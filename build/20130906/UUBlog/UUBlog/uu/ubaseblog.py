#-*- coding:utf-8 -*-
import os
import importlib

from django.http import HttpResponseRedirect 

from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.common import utility,pub

from UUBlog.models import *

from UUBlog.init import *


class UBaseBlogView(UBaseTemplateView):
    
    def __init__(self, **kwargs):
        super(UBaseBlogView, self).__init__(**kwargs)

        
        self.options={}
        self.user=None
        self.navs={}

        self.theme="default"
        self.themeConfig={}

    def InitValue(self):

        self.options=self.GetOptions()
        self.user=self.request.user
        

        self.navs={}
        self.navs["main"]=self.BuildNavTreeHtml(0)
        self.navs["top"]={}
        self.navs["top"]["left"]=self.GetNavList(position=2,align=1)
        self.navs["top"]["right"]=self.GetNavList(position=2,align=3)
        self.navs["bottom"]=self.GetNavList(position=3)
        
        self.theme=self.GetOption("theme","default")

        themeModuleName="%s.%s.%s" %("UUBlog.templates.themes",self.theme,"config")
        self.themeConfig=importlib.import_module(themeModuleName).config

        

    def post_context_data(self, **kwargs):
        context= super(UBaseBlogView, self).post_context_data(**kwargs)
       
        self.InitValue()

        myContext=self.PostContext(**kwargs)
        
        self.AddVars(context,myContext)

        return context


    def get_context_data(self, **kwargs):
        context= super(UBaseBlogView, self).get_context_data(**kwargs)

        self.InitValue()

        myContext=self.GetContext(**kwargs)
        self.AddVars(context,myContext)

        return context

    def SetTemplateName(self,templateName):
        self.template_name="themes/%s/%s.html" %(self.theme,templateName)

    def GetHookList(self,key):
        global G
       
        if G["hooks"].has_key(key):
            return G["hooks"][key]
        return []

    #模块列表
    def GetWidgetList(self,sid="normal",isRender=True):
        if sid is None or sid=="":
            sid="normal"

        #获取博客的widget
        myWidgetList=MyWidget.objects.order_by("-sortnum").filter(sidebar_id=sid)
            
        if not isRender :
            return  myWidgetList

        global G
        retWidgetList=[]

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

    #导航
    def GetNavList(self,parentId=-1,position=None,align=None):
        navList=Navigate.objects.order_by("position","-sortnum")
        if parentId>-1:
            navList=navList.filter(parent_id=parentId)
        if position:
            navList=navList.filter(position=position)
        if align:
            navList=navList.filter(align=align)
        return navList

    def BuildNavTreeHtml(self,pId,level=-1,theId=-1):
        navs=self.GetNavList(pId,1)

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
        navList=self.GetNavList(pId,position)

        if navList is None or len(navList)==0:
            return ""

        level+=1

        options ="data[%s]=[" %pId
        for nav in navList:
            if nav.id==theId:
                continue
            options+="[%s,%s,'%s','%s','%s',%s]," %(nav.parent_id,nav.id,nav.name,nav.alias,nav.url,nav.sortnum)
        options=options.rstrip(",")+"];"

        for nav in navList:
            if nav.id==theId:
                continue

            options+=self.BuildNavTreeJs(nav.id,position,level,theId)
        return options

    #文章分类
    def GetCatList(self,parentId=-1):

        categoryList=Category.objects.order_by("-sortnum")
        if parentId>-1:
            categoryList=categoryList.filter(parent_id=parentId)
        return categoryList

    def BuildCatTreeJs(self,pId,level=-1,theId=-1):
        catList=self.GetCatList(pId)

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
        catList=self.GetCatList(pId)

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

    #侧边栏
    def GetSidebarList(self):
        return Sidebar.objects.all()

    #文章列表
    def GetPostList(self,*orders,**kwargs):
        postList=Post.objects.all()
        if kwargs:
            postList=postList.filter(**kwargs)
        if orders:
            for order in orders:
                postList=postList.order_by(order)
        else:
            postList=postList.order_by("-createtime")

        return postList

    def GetPost(self,postId):
        try:
            postInfo=Post.objects.get(id=postId)
        except:
            postInfo=None
        return postInfo

    #页面列表
    def GetPageList(self,*orders,**kwargs):
        pageList=Page.objects.all()
        if kwargs:
            pageList=pageList.filter(**kwargs)
        if orders:
            for order in orders:
                pageList=pageList.order_by(order)
        else:
            pageList=pageList.order_by("-createtime")
        return pageList

    def GetPage(self,pageId):
        try:
            pageInfo=Page.objects.get(id=pageId)
        except:
            pageInfo=None
        return pageInfo

    #评论列表
    def GetCommentList(self,*orders,**kwargs):
        commentList=Comment.objects.all()
        if kwargs:
            commentList=commentList.filter(**kwargs)
        if orders:
            for order in orders:
                commentList=commentList.order_by(order)
        else:
            commentList=commentList.order_by("-createtime")

        return commentList

    def GetComment(self,commentId):
        try:
            commentInfo=Comment.objects.get(id=commentId)
        except:
            commentInfo=None
        return commentInfo

    #获取一个Option的值
    def GetOption(self,name,default=None):
        optionList=Option.objects.filter(name=name)
        if optionList:
            return optionList[0].value
        
        return default

    #修改或增加（isCreate为True时）一个Option
    def UpdateOption(self,name,value="",isCreate=True):
        optionValue=self.GetOption(name)
        if optionValue and optionValue==value:
            return

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

    #获取所有的Option
    def GetOptions(self):
        ret={}
        optionList=Option.objects.all()

        for optionInfo in optionList:
            ret.setdefault(optionInfo.name,optionInfo.value)

        return ret
         
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
