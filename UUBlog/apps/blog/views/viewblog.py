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



def createBlog(user):
  
    blog=Blog()
    blog.id=user.id
    blog.title=user.username+"的博客".decode("utf-8")
    blog.modules="profile,category,hotarticlelist,hotcommentlist,followbloglist"
    blog.template="default"
    blog.createtime=datetime.datetime.now()
    blog.save()

#博客信息
@login_required()
def base(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]
    typeList=Type.objects.filter(parent_id=0)
    myTypeList=currentBlog.types.split(",")
    myTypeIds=[]
    for tId in myTypeList:
        if tId!="":
            myTypeIds.append(int(tId))
            #myTypeIds.append("%s" %bt.type_id)

    if pub.HasPostData(request,"ok"):
        currentBlog.title=pub.GetPostData(request,"title")
        currentBlog.description=pub.GetPostData(request,"description")
        currentBlog.keywords=pub.GetPostData(request,"keywords")
        currentBlog.about=pub.GetPostData(request,"about")
        currentBlog.announcement=pub.GetPostData(request,"announcement")
        currentBlog.types=pub.GetPostData(request,"typeids")
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/base.html",locals())

#头像
@login_required()
def avatar(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]

    #000/00/01
    if pub.HasPostData(request,"ok"):
        avatarPath=("%d" %currentBlog.id).rjust(7,"0")
        dir1=avatarPath[0:3]
        dir2=avatarPath[3:5]
        fileName=avatarPath[5:7]
        path="%s/%s/%s/" %("blog/avatar",dir1,dir2)

        currentBlog.avatar=pub.SaveFile(request.FILES['avatar'],path,fileName)
      
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/avatar.html",locals())

#模板设置
@login_required()
def template(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]

    if pub.HasPostData(request,"ok"):
        currentBlog.template=pub.GetPostData(request,"template")
       
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/template.html",locals())

#样式设置
@login_required()
def style(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]

    if pub.HasPostData(request,"ok"):
        currentBlog.css=pub.GetPostData(request,"css")
        currentBlog.headhtml=pub.GetPostData(request,"headhtml")
        currentBlog.footerhtml=pub.GetPostData(request,"footerhtml")
  
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/style.html",locals())

#域名设置
@login_required()
def domain(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]


    if pub.HasPostData(request,"ok"):
        currentBlog.domain=pub.GetPostData(request,"domain")
  
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/domain.html",locals())



#模块设置
@login_required()
def module(request,uid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    currentBlog=userInfos["currentblog"]

    allModules={}
    for key,value in modules.moduleList.items():
        allModules.setdefault(key,value["name"])

    tempModules=currentBlog.modules.split(",")
    myModules={}
    for tempModule in tempModules:
        moduleName=modules.GetModuleName(tempModule)
        if moduleName:
            myModules.setdefault(tempModule,moduleName)


    if pub.HasPostData(request,"ok"):
        tempModules=pub.GetPostData(request,"modules").split(",")
        retModules=""
        for key in tempModules:
            if modules.moduleList.has_key(key):
                retModules+=key+","
                

        currentBlog.modules=retModules
  
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"blog/pub/module.html",locals())