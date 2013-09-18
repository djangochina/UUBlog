#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView

from UUBlog.models import *

from UUBlog.common import utility,pub

from UUBlog.views import widgets
from UUBlog.init import *
import os
import importlib

class UBaseBlogView(UBaseTemplateView):

    theme="themes/default"
    
    def __init__(self, **kwargs):
        super(UBaseBlogView, self).__init__(**kwargs)

        self.user=None
        self.navigate={}
        self.options={}
        self.theme="default"
        self.themeConfig={}

    def InitValue(self):

        self.user=self.request.user
        self.options=self.GetOptions()

        self.navigate={}
        self.navigate["main"]=self.BuildNavTreeHtml(0)
        self.navigate["top"]={}
        self.navigate["top"]["left"]=self.GetNavigateList(position=2,align=1)
        self.navigate["top"]["right"]=self.GetNavigateList(position=2,align=3)
        self.navigate["bottom"]=self.GetNavigateList(position=3)

        
        self.theme=self.GetOption("theme","default")

        themeModuleName="%s.%s.%s" %("UUBlog.templates.themes",self.theme,"config")
        self.themeConfig=importlib.import_module(themeModuleName).config

    def post_context_data(self, **kwargs):
        context= super(UBaseBlogView, self).post_context_data(**kwargs)
       
        self.InitValue()

        myContext=self.PostContext(**kwargs)
        
        self.AddVars(context,myContext)

        self.AddVars(context,locals())

        return context


    def get_context_data(self, **kwargs):
        context= super(UBaseBlogView, self).get_context_data(**kwargs)

        self.InitValue()

        myContext=self.GetContext(**kwargs)
        self.AddVars(context,myContext)

        self.AddVars(context,locals())

        return context

    def SetTemplateName(self,templateName):
        self.template_name="%s/%s/%s.html" %("themes",self.theme,templateName)

    def GetHookList(self,key):
        global G
       
        if G["hooks"].has_key(key):
            return G["hooks"][key]
        return []

    #我的模块列表
    def GetMyWidgetList(self):
        
        global G
        retWidgetList=[]

        #获取博客的widget
        myWidgetList=MyWidget.objects.order_by("-sortnum")
            
            
        for myWidget in myWidgetList:

            widgetName=myWidget.widget

            widgetValue={}
                
            widgetValue.setdefault("name",widgetName)

            widgetValue.setdefault("id",myWidget.id)
            widgetValue.setdefault("title",myWidget.title)
            widgetValue.setdefault("isshowtitle",myWidget.isshowtitle)
            widgetValue.setdefault("params",utility.Json2Obj(myWidget.params))

            data=utility.Json2Obj(myWidget.data)

            if G["widgets"].has_key(widgetName):

                widgetModule=G["widgets"][widgetName]

                widgetView=widgetModule.config["view"]
                if widgetView and callable(widgetView):
                    data=widgetView(self,myWidget)

            widgetValue.setdefault("data",data)

            retWidgetList.append(widgetValue)

        return retWidgetList

    def GetNavigateList(self,parentId=-1,position=None,align=None):
        navList=Navigate.objects.order_by("position","-sortnum")
        if parentId>-1:
            navList=navList.filter(parent_id=parentId)
        if position:
            navList=navList.filter(position=position)
        if align:
            navList=navList.filter(align=align)
        return navList

    def BuildNavTreeHtml(self,pId,level=-1,theId=-1):
        navs=self.GetNavigateList(pId,1)

        if navs is None or len(navs)==0:
            return ""

        level+=1

        if level==0:
            options="<ul class='navs_%s sf-menu' id='mainNav'>" %(level)
        else:
            options="<ul class='navs_%s childNavs'>" %(level)

        for nav in navs:
            if nav.id==theId:
                continue

            options+="<li class='leval_%s' ><a href='%s' target='%s'>%s</a>" %(level,nav.url,nav.target,nav.alias)
            
            options+=self.BuildNavTreeHtml(nav.id,level,theId)

            options+="</li>"

        options+="</ul>"
        return options

    def BuildNavTreeJs(self,pId,position,level=-1,theId=-1):
        navList=self.GetNavigateList(pId,position)

        if navList is None or len(navList)==0:
            return ""

        level+=1

        options ="data[%s]=[" %pId
        for nav in navList:
            if nav.id==theId:
                continue
            options+="[%s,%s,'%s','%s','%s']," %(nav.parent_id,nav.id,nav.name,nav.alias,nav.url)
        options=options.rstrip(",")+"];"

        for nav in navList:
            if nav.id==theId:
                continue

            options+=self.BuildNavTreeJs(nav.id,position,level,theId)
        return options

    #文章分类
    def GetCategoryList(self,parentId=-1):

        categoryList=Category.objects.order_by("-sortnum")
        if parentId>-1:
            categoryList=categoryList.filter(parent_id=parentId)
        return categoryList

    def BuildCatTreeJs(self,pId,level=-1,theId=-1):
        catList=self.GetCategoryList(pId)

        if catList is None or len(catList)==0:
            return ""

        level+=1

        options="data[%s]=[" %pId
        for cat in catList:
            if cat.id==theId:
                continue
            options+="[%s,%s,'%s','%s',%s,%s,%s]," %(cat.parent_id,cat.id,cat.name,cat.alias,cat.posts,cat.sortnum,level)
        options=options.rstrip(",")+"];"

        for cat in catList:
            if cat.id==theId:
                continue

            options+=self.BuildCatTreeJs(cat.id,level,theId)
        return options

    def BuildCatTreeHtml(self,pId,level=-1):
        catList=self.GetCategoryList(pId)

        if catList is None or len(catList)==0:
            return ""

        level+=1

        if level==0:
            options="<ul class='cats_%s' id='catTree'>" %(level)
        else:
            options="<ul class='cats_%s childCats'>" %(level)

        for cat in catList:
            
            options+="<li class='leval_%s' ><a href='/cat/%s/' >%s</a>" %(level,cat.id,cat.name)
            
            options+=self.BuildCatTreeHtml(cat.id,level)

            options+="</li>"

        options+="</ul>"
        return options

    #文章列表
    def GetPostList(self,*order,**kwargs):
        postList=Post.objects.order_by("-createtime")
        if kwargs:
            postList=postList.filter(**kwargs)
        
        return postList


    #添加访客
    def AddVisit(self,uid):
        pass
        #if self.currentUser and not self.IsMyBlog(uid):
        #    visit=Visit.objects.filter(blog_id=self.currentBlog.id,visit_blog_id=self.guestBlog.id)
        #    if not visit:
        #        visit=Visit()
        #        visit.blog_id=self.currentBlog.id
        #        visit.visit_blog_id=self.guestBlog.id
        #        visit.lastvisittime=datetime.datetime.now()
        #        visit.save()

    def GetOption(self,name,default=None):
        optionList=Option.objects.filter(name=name)
        if optionList:
            return optionList[0].value
        
        return default

    def AddOption(self,name,value=""):
        optionInfo=Option()
        optionInfo.name=name
        optionInfo.value=value
        optionInfo.save()

    def UpdateOption(self,name,value="",isCreate=True):
        optionList=Option.objects.filter(name=name)
        
        if optionList:
            optionInfo= optionList[0]
            optionInfo.value=value
            optionInfo.save()
        elif isCreate:
            optionInfo=Option()
            optionInfo.name=name
            optionInfo.value=value
            optionInfo.save()

    def GetOptions(self):
        ret={}
        optionList=Option.objects.all()

        for optionInfo in optionList:
            ret.setdefault(optionInfo.name,optionInfo.value)

        return ret
         