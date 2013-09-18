#-*- coding:utf-8 -*-
import os
import importlib
import uuid
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

        themeList=[]

        dirs=os.listdir("UUBlog/templates/themes")
        for dir in dirs:
            if dir.find(".")>0:
                continue
            themeModuleName="%s.%s.%s" %("UUBlog.templates.themes",dir,"config")
            themeList.append(importlib.import_module(themeModuleName).config)

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


class HeaderStyleView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        self.template_name="admin/headerstyle.html"
        

        return locals()

    def PostContext(self, **kwargs):
        uploaded_file = self.GetFile("headerstyle_image")
        if uploaded_file:
            currentTime=datetime.datetime.now()
            path="\\%s\\%s\\%s" %("attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
            fileName="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())

        
            uploadFileInfo=pub.SaveFile(uploaded_file,path,fileName)
            attachInfo=Attachment()
            attachInfo.path=uploadFileInfo["path"]
            attachInfo.name=uploadFileInfo["newname"]
            attachInfo.title=uploadFileInfo["name"]
            attachInfo.description=uploadFileInfo["name"]
            attachInfo.extension=uploadFileInfo["ext"]

            filetype=10
            if attachInfo.extension in self.options["filetype_image"]:
                filetype=1
            elif attachInfo.extension in self.options["filetype_media"]:
                filetype=2
            elif attachInfo.extension in self.options["filetype_file"]:
                filetype=3

            attachInfo.filetype=filetype
            attachInfo.createtime=datetime.datetime.now()

            attachInfo.save()

            self.UpdateOption("headerstyle_image",self.GetPostData("headerstyle_image",uploadFileInfo["path"]))

        self.UpdateOption("headerstyle_repeat",self.GetPostData("headerstyle_repeat","no-repeat"))
        self.UpdateOption("headerstyle_horizontal",self.GetPostData("headerstyle_horizontal","center"))
        self.UpdateOption("headerstyle_vertical",self.GetPostData("headerstyle_vertical","top"))
        self.UpdateOption("headerstyle_color",self.GetPostData("headerstyle_color","transparent"))
        self.UpdateOption("headerstyle_height",self.GetPostData("headerstyle_height","0"))
        self.UpdateOption("headerstyle_status",self.GetPostData("headerstyle_status","none"))


       
        return locals()

class BackgroundStyleView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        self.template_name="admin/backgroundstyle.html"
        

        return locals()

    def PostContext(self, **kwargs):
        uploaded_file = self.GetFile("backgroundstyle_image")
        if uploaded_file:
            currentTime=datetime.datetime.now()
            path="\\%s\\%s\\%s" %("attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
            fileName="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())

        
            uploadFileInfo=pub.SaveFile(uploaded_file,path,fileName)
            attachInfo=Attachment()
            attachInfo.path=uploadFileInfo["path"]
            attachInfo.name=uploadFileInfo["newname"]
            attachInfo.title=uploadFileInfo["name"]
            attachInfo.description=uploadFileInfo["name"]
            attachInfo.extension=uploadFileInfo["ext"]

            filetype=10
            if attachInfo.extension in self.options["filetype_image"]:
                filetype=1
            elif attachInfo.extension in self.options["filetype_media"]:
                filetype=2
            elif attachInfo.extension in self.options["filetype_file"]:
                filetype=3

            attachInfo.filetype=filetype
            attachInfo.createtime=datetime.datetime.now()

            attachInfo.save()

            self.UpdateOption("backgroundstyle_image",self.GetPostData("headerstyle_image",uploadFileInfo["path"]))

        self.UpdateOption("backgroundstyle_repeat",self.GetPostData("backgroundstyle_repeat","no-repeat"))
        self.UpdateOption("backgroundstyle_horizontal",self.GetPostData("backgroundstyle_horizontal","center"))
        self.UpdateOption("backgroundstyle_vertical",self.GetPostData("backgroundstyle_vertical","top"))
        self.UpdateOption("backgroundstyle_fix",self.GetPostData("backgroundstyle_fix","False"))
        self.UpdateOption("backgroundstyle_color",self.GetPostData("backgroundstyle_color","transparent"))
        self.UpdateOption("backgroundstyle_status",self.GetPostData("backgroundstyle_status","none"))
       
        return locals()




























