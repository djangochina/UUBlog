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
from UUBlog.apps.blog import modules

def index(request,tid=-1,order='suggestes'):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    typeList=Type.objects.filter(parent_id=0)
    
    #currentType=Type.objects.get(id=tid)
    #childrenType=Type.objects.filter(parent_id=tid)

    #sql='''
    #SELECT blog.* 
    #    FROM  `blog_blog` blog
    #    INNER JOIN blog_blogtype blogtype ON blog.id = blogtype.blog_id
    #    INNER JOIN blog_type type ON type.id = blogtype.type_id 
    #'''
    #sql="%s WHERE type.id =%s" %(sql,tid)
    #blogList=Blog.objects.raw(sql)

    if tid>0:
        blogList=Blog.objects.filter(types__contains=("%s," %tid))
        currentType=Type.objects.get(id=tid)
    else:
        blogList=Blog.objects.all()
        currentType=None
    blogList=blogList.order_by("-%s" %order)

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/space.html",locals())



def popular(request,tid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    typeList=Type.objects.filter(parent_id=0)
    currentType=Type.objects.get(id=tid)
    childrenType=Type.objects.filter(parent_id=tid)

    blogList=Blog.objects.filter(types__contains=("%s," %tid))

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/space.html",locals())


def suggest(request,tid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    typeList=Type.objects.filter(parent_id=0)
    currentType=Type.objects.get(id=tid)
    childrenType=Type.objects.filter(parent_id=tid)

    blogList=Blog.objects.filter(types__contains=("%s," %tid))

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/space.html",locals())


def suggestnew(request,tid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    typeList=Type.objects.filter(parent_id=0)
    currentType=Type.objects.get(id=tid)
    childrenType=Type.objects.filter(parent_id=tid)

    blogList=Blog.objects.filter(types__contains=("%s," %tid))

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/space.html",locals())


def follow(request,tid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    typeList=Type.objects.filter(parent_id=0)
    currentType=Type.objects.get(id=tid)
    childrenType=Type.objects.filter(parent_id=tid)


    blogList=Blog.objects.filter(types__contains=("%s," %tid))

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/space.html",locals())