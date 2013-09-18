#-*- coding:utf-8 -*-

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
from UUBlog.models import *
from UUBlog.uu.ubaseadmin import UBaseAdminView

from UUBlog.init import *

class ThemeManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        categoryList=self.GetCategoryList()

        self.template_name="admin/themelist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            theme=self.GetPostData("theme","default")

            self.UpdateOption("theme",theme)
            
        return locals()

class ThemeEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        categoryInfo=Category.objects.get(id=cid)

        self.template_name="blog/pub/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()
        
        self.returnUrl=categoryroot %self.currentUser.id
        return locals()

class ThemeDeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()

class WidgetManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        global G

        widgetList=G["widgets"]

        myWidgetList=self.GetMyWidgetList()

        self.template_name="admin/widgetlist.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData('ok'):
            global G

            widgets=self.GetRequestListData("widget")

            for widgetName in widgets:

                widgetModule=G["widgets"][widgetName]

                myWidget=MyWidget()
                myWidget.widget=widgetModule.config["name"]
                myWidget.title=widgetModule.config["title"]
                myWidget.isshowtitle=True
                myWidget.params=widgetModule.config["initparams"]
                myWidget.data=widgetModule.config["initdata"]
                myWidget.sortnum=0

                myWidget.save()
        return locals()

class WidgetEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        wid=int(kwargs.get("wid",0))
        
        widgetInfo=MyWidget.objects.get(id=wid)

        self.template_name="admin/widget.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()
        
        self.returnUrl=categoryroot %self.currentUser.id
        return locals()

class WidgetDeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()
    

class NavManagerView(UBaseAdminView):

    def GetContext(self, **kwargs):

        position=int(self.GetDicData(kwargs,"p",'1'))

        navTree="var data=Array();"
        navTree+=self.BuildNavTreeJs(0,position,-1,-1)

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)
        
        navList=self.GetNavigateList(None,position)

        self.template_name="admin/navlist.html"

        return locals()

    def PostContext(self, **kwargs):
        position=self.GetDicData(kwargs,"p",1)

        if self.HasPostData('ok'):

            parent_id=self.GetPostData("parentId",0)
            name=self.GetPostData("name")            
            url=self.GetPostData("url")
            align=self.GetPostData("align",1)
           
            navInfo=Navigate(parent_id=parent_id,position=position,name=name,url=url,alias=name)
            navInfo.align=align
            navInfo.save()

        if self.HasPostData("okCat"):
            catIds=self.GetRequestListData("catTree")
            for catId in catIds:
                catInfo=Category.objects.get(id=catId)

                navInfo=Navigate(parent_id=0,position=position)
                navInfo.name=catInfo.name
                navInfo.alias=catInfo.name
                navInfo.url="/cat/%s/" %catId

                navInfo.save()


        self.returnUrl="/admin/navlist/position/%s/" %position

        return locals()

class NavEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        position=self.GetDicData(kwargs,"p",1)

        nid=int(self.GetDicData(kwargs,"nid",-1))
     
        navTree="var data=Array();"
        navTree+=self.BuildNavTreeJs(0,position,-1,nid)
       
        if nid>-1:
            navInfo=Navigate.objects.get(id=nid)

        self.template_name="admin/nav.html"

        return locals()

    def PostContext(self, **kwargs):
        
        if self.HasPostData('ok'):
            
            position=self.GetDicData(kwargs,"p",1)

            parent_id=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            description=self.GetPostData("description")
            
            align=self.GetPostData("align")
            url=self.GetPostData("url")
            target=self.GetPostData("target")
            fontstyle=self.GetPostData("fontstyle")
            isenable=self.GetPostData("isenable",0)
            sortnum=self.GetPostData("sortnum",0)
           
            navInfo=Navigate()

            nid=self.GetDicData(kwargs,"nid",None)

            if nid:
                try:
                    navInfo=Navigate.objects.get(id=nid)
                except:
                    pass
            
            navInfo.parent_id=parent_id
            navInfo.name=name
            navInfo.name=name
            navInfo.alias=alias
            navInfo.description=description
            navInfo.position=position
            navInfo.align=align
            navInfo.url=url
            navInfo.target=target
            navInfo.fontstyle=fontstyle
            navInfo.isenable=isenable
            navInfo.sortnum=0 if sortnum=="" else int(sortnum)

            navInfo.save()

            self.returnUrl="/admin/navlist/position/%s/" %position
        return locals()

class NavDeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()


class FileManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        categoryList=self.GetCategoryList()

        self.template_name="admin/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData('ok'):
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category()
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.save()

        return locals()

class FileEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        categoryInfo=Category.objects.get(id=cid)

        self.template_name="blog/pub/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()
        
        self.returnUrl=categoryroot %self.currentUser.id
        return locals()

class FileDeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()


























