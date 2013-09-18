#-*- coding:utf-8 -*-
import json

from django.shortcuts import get_object_or_404, render
from django.http import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import time,datetime
from django.db.models import Q
from django.db import connection
from django.template import RequestContext 
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from UUBlog.common import pub,utility
from UUBlog.apps.accounts.models import UserProfile
from UUBlog.apps.accounts.views import viewaccounts
from UUBlog.apps.blog.models import *
from UUBlog.apps.blog.views.baseblogview import *

from UUBlog.apps.blog import modules

def createBlog(user):
  
    blog=Blog()
    blog.id=user.id
    blog.title=user.username+"的博客".decode("utf-8")
    blog.description="欢迎来".decode("utf-8")+user.username+"的博客".decode("utf-8")
    blog.keywords=user.username
    #blog.modules="profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist"
    blog.template="default"
    blog.createtime=datetime.datetime.now()
    blog.save()

    defaultWidgetList=["profile","category","hotarticlelist","hotcommentlist","followbloglist","bevisitbloglist"]
    for widgetName in defaultWidgetList:

        CreateBlogWidget(blog.id,widgetName)


class IndexView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        tid=int(kwargs.get("tid",-1))
        order=kwargs.get("order","suggestes")

        typeList=Type.objects.filter(parent_id=0)

        if tid>0:
            blogList=Blog.objects.filter(types__contains=("%s," %tid))
            currentType=Type.objects.get(id=tid)
        else:
            blogList=Blog.objects.all()
            currentType=None

        blogList=blogList.order_by("-%s" %order)
        blogListTodayViews=Blog.objects.order_by("-todayviews")[0:30]

        followBlogIds=self.GetFollowBlogIds(uid)

        self.template_name="blog/blog.html"

        return locals()

class BaseView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
       
        typeList=Type.objects.filter(parent_id=0)
        myTypeArray=self.currentBlog.types.split(",")
        myTypeIds=[]
        for tId in myTypeArray:
            if tId!="":
                myTypeIds.append(int(tId))

        self.template_name="blog/pub/base.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.title=self.GetPostData("title")
            self.currentBlog.description=self.GetPostData("description")
            self.currentBlog.keywords=self.GetPostData("keywords")
            self.currentBlog.about=self.GetPostData("about")
            self.currentBlog.announcement=self.GetPostData("announcement")
            types=""
            blogTypes=self.GetRequestListData("blogType")
            for type in blogTypes:
                types+="%s," %type
            self.currentBlog.types=types
            self.currentBlog.save()

        return locals()

class AvatarView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="blog/pub/avatar.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        #000/00/01
        if self.HasPostData("ok") and self.request.FILES['avatar']:
            avatarPath=("%d" %self.currentBlog.id).rjust(7,"0")
            dir1=avatarPath[0:3]
            dir2=avatarPath[3:5]
            fileName=avatarPath[5:7]
            path="%s/%s/%s/" %("blog/avatar",dir1,dir2)

            self.currentBlog.avatar=pub.SaveFile(self.request.FILES['avatar'],path,fileName)[0]
      
            self.currentBlog.save()


        return locals()

class TemplateView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        skins=["default","temp1"]
        self.template_name="blog/pub/template.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.template=self.GetPostData("template")
           
            self.currentBlog.save()

        return locals()

class StyleView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="blog/pub/style.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.css=self.GetPostData("css")
            self.currentBlog.headhtml=self.GetPostData("headhtml")
            self.currentBlog.footerhtml=self.GetPostData("footerhtml")
           
            self.currentBlog.save()

        return locals()

class DomainView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="blog/pub/domain.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.domain=self.GetPostData("domain")
            
            self.currentBlog.save()

        return locals()

class WidgetView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        allWidgetList=Widget.objects.order_by("sortnum")

        myBlogWidgetList=BlogWidget.objects.filter(blog_id=self.currentBlog.id).order_by("-sortnum")
        self.template_name="blog/pub/widget.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
           
            myWidgetNameList=self.GetRequestListData("allWidgets")

            for widgetName in myWidgetNameList:
                CreateBlogWidget(self.currentBlog.id,widgetName)
               
        return locals()

class WidgetCreateView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        allWidgetList=Widget.objects.all()

        myBlogWidgetList=BlogWidget.objects.filter(blog_id=self.currentBlog.id)

        self.template_name="blog/pub/widgetcreate.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
           
            myWidgetNameList=self.GetRequestListData("myModules")

            for widgetName in myWidgetNameList:
                
                isExist=BlogWidget.objects.filter(widget=widgetName)
                if isExist:
                    continue

                widgetInfo=Widget.objects.get(name=widgetName)

                blogWidgetInfo=BlogWidget()
                blogWidgetInfo.blog_id=self.currentBlog.id
                blogWidgetInfo.widget=widgetInfo.name
                blogWidgetInfo.title=widgetInfo.title

                if widgetInfo.issys==1:
                    import json
                    blogWidgetInfo.params='{"udi":%s}' %self.currentBlog.id

                blogWidgetInfo.save()
          
        return locals()

def CreateBlogWidget(blogId,widgetName):
    widgetInfo=Widget.objects.get(name=widgetName)

    blogWidgetInfo=BlogWidget()
    blogWidgetInfo.blog_id=blogId
    blogWidgetInfo.widget=widgetInfo
    blogWidgetInfo.title=widgetInfo.title
                
    #params
    if widgetInfo.datafrom=="func":
        blogWidgetInfo.params='{"uid":%s}' %blogId

    #attvalues
    attDef=utility.Json2Obj(widgetInfo.attdef,None)
    if attDef is not None:
        attValues={}
        for att in attDef:
            attValues.setdefault(att["name"],'')

        blogWidgetInfo.attvalues=utility.Obj2Json(attValues)

    #datavalues
    blogWidgetInfo.datavalues=widgetInfo.defaultdata

    blogWidgetInfo.save()

#widget 设置
class WidgetSettingView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        wid=int(kwargs.get("wid",0))

        blogWidgetInfo=BlogWidget.objects.get(id=wid)
        
        widgetInfo=blogWidgetInfo.widget

        #------begin 属性信息---------
        attDefList=utility.Json2Obj(widgetInfo.attdef,None)
        attHtml=None
        if attDefList is not None:
            attValues=utility.Json2Obj(blogWidgetInfo.attvalues,None)
            attHtml="";
        
            for attDef in attDefList:
                attName=attDef["name"]
                attLable=attDef["label"]
                attForm=attDef["form"]
                attValue=attDef["value"]

                attMyValue=attValues[attName]

                label='<label for="%s">%s</label>' %(attName,attLable)
                form=""
                if attForm=="text":
                    form='<input name="%s" id="%s" type="text" width="60" value="%s">' %(attName,attName,attMyValue)
                elif attForm=="select":
                    options=""
                    valueArray=attValue.split(",")
                    for value in valueArray:
                        selected=''
                        if value==attMyValue:
                            selected=' selected="selected" '
                        options+='<option value="%s" %s>%s</option>' %(value,selected,value)
                    form='<select name="%s" id="%s">%s</select>' %(attName,attName,options)
                elif attForm=="radio" or attForm=="checkbox":
                    form=""
                    valueArray=attValue.split(",")
                    for value in valueArray:
                        checked=''
                        if value==attMyValue:
                            checked='checked="checked"'
                        form+='<input name="%s" id="%s" type="%s" value="%s" %s>%s' %(attName,attName,attForm,value,checked,value)
      
                attHtml+=label+form
        #-------end 属性信息--------

        dataItem=None
        if widgetInfo.datafrom=="url" or widgetInfo.datafrom=="html":
            dataItem='<textarea name="datavalues" %s >%s</textarea>' %('' if widgetInfo.canedit else 'disabled="disabled"',blogWidgetInfo.datavalues)
            
        elif widgetInfo.datafrom=="json":
            jsonColumnDefList=utility.Json2Obj(widgetInfo.jsondef)
            jsonColumnsCount=len(jsonColumnDefList)

            dataValues=utility.Json2Obj(blogWidgetInfo.datavalues)  
       
            dataItem=''
            for myData in dataValues:
                dataItem+='<tr>'
                for jsonColumn in jsonColumnDefList:
                    columnName=jsonColumn["name"]

                    dataItem+='<td><input id="%s" name="%s" type="text" width="60" value="%s" %s/></td>' %(columnName,columnName,myData[columnName],'' if widgetInfo.canedit else 'disabled="disabled"')
                dataItem+='</tr>'

        elif widgetInfo.datafrom=="func":
            pass
        elif widgetInfo.datafrom=="sql":
            pass
        elif widgetInfo.datafrom=="block":
            pass

        self.template_name="blog/pub/widgetsetting.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        wid=int(kwargs.get("wid",0))

        if self.HasPostData("ok"):
            blogWidgetInfo=BlogWidget.objects.get(id=wid)
            widgetInfo=blogWidgetInfo.widget

            #设置标题
            blogWidgetInfo.title=self.GetPostData("title")

            #---------begin 设置参数信息--------
            #widget的属性信息
            attDefList=utility.Json2Obj(widgetInfo.attdef,None)
            if attDefList is not None:
                attValues={}
                for att in attDefList:
                    attName=att["name"]
                    attLable=att["label"]
                    attForm=att["form"]
                    attValue=att["value"]

                    if attForm=="checkbox":
                        value=self.GetRequestListData(attName)
                    else:
                        value=self.GetPostData(attName)
                    attValues.setdefault(attName,value)
            
                blogWidgetInfo.attvalues=utility.Obj2Json(attValues)
            #---------end 设置参数信息--------

            #---------begin 设置数据信息 datavalues-----------
            if widgetInfo.datafrom=="url" or widgetInfo.datafrom=="html":
                if widgetInfo.canedit:
                    blogWidgetInfo.datavalues=self.GetPostData("datavalues")
            elif widgetInfo.datafrom=="json" and widgetInfo.canedit:
                jsonColumnDefList=utility.Json2Obj(widgetInfo.jsondef,None)
            
                #列数
                jsonColumnsCount=len(jsonColumnDefList)

                #获取form表单中每一列的数据
                postDataColumnList=[]
                for jsonColumn in jsonColumnDefList:
                    postDataColumnList.append(self.request.POST.getlist(jsonColumn["name"]))

                
                #行数
                dataRowsCount=len(postDataColumnList[0])

                dataValues=[]
                for rowIndex in range(dataRowsCount):
                    dataItem={}
                    for columnIndex in range(jsonColumnsCount):
                        columnName=jsonColumnDefList[columnIndex]["name"]
                        dataResult=postDataColumnList[columnIndex][rowIndex]
                        dataItem.setdefault(columnName,dataResult)
                    dataValues.append(dataItem)
           
                blogWidgetInfo.datavalues=utility.Obj2Json(dataValues)

            elif widgetInfo.datafrom=="func":
                pass
            elif widgetInfo.datafrom=="sql":
                pass
            elif widgetInfo.datafrom=="block":
                pass
            #---------end 设置数据信息-----------

            blogWidgetInfo.sortnum=int(self.GetPostData("sortnum",0))


            blogWidgetInfo.save()

        return locals()




































