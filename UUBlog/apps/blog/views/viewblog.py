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
    blog.modules="profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist"
    blog.template="default"
    blog.createtime=datetime.datetime.now()
    blog.save()

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
            self.currentBlog.types=self.GetPostData("typeids")
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

            self.currentBlog.avatar=pub.SaveFile(self.request.FILES['avatar'],path,fileName)
      
            self.currentBlog.save()


        return locals()

class TemplateView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
       
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

class ModuleView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        allModules={}
        for key,value in modules.moduleList.items():
            allModules.setdefault(key,value["name"])

        myModuleArray=self.currentBlog.modules.split(",")
        myModules={}
        for myModuleKey in myModuleArray:
            moduleName=modules.GetModuleName(myModuleKey)
            if moduleName:
                myModules.setdefault(myModuleKey,moduleName)


        self.template_name="blog/pub/module.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.domain=self.GetPostData("domain")
            
            self.currentBlog.save()

            myModuleArray=pub.GetPostData(request,"modules").split(",")
            retModules=""
            for key in myModuleArray:
                if modules.moduleList.has_key(key):
                    retModules+=key+","
                

            currentBlog.modules=retModules
  
            currentBlog.save()

        return locals()
