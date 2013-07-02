#-*- coding:utf-8 -*-

import time,datetime

from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

from django.views.generic.base import TemplateView
from django.views import generic
from django.db.models import Q
from django.db import connection
from django.template import RequestContext 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth
from UUBlog.models import Category, Article,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import common

import utility
import modules


#博客信息
@login_required()
def blog(request,uid=-1):
    userInfos=common.Users(request,-1)
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


    if utility.HasPostData(request,"ok"):
        currentBlog.domain=utility.GetPostData(request,"domain")
        currentBlog.title=utility.GetPostData(request,"title")
        currentBlog.description=utility.GetPostData(request,"description")
        currentBlog.keywords=utility.GetPostData(request,"keywords")
        currentBlog.about=utility.GetPostData(request,"about")
        currentBlog.announcement=utility.GetPostData(request,"announcement")

        tempModules=utility.GetPostData(request,"modules").split(",")
        retModules=""
        dot=""
        for key in tempModules:
            if modules.moduleList.has_key(key):
                retModules+=dot+key
                dot=","

        currentBlog.modules=retModules
        currentBlog.template=utility.GetPostData(request,"template")
        currentBlog.css=utility.GetPostData(request,"css")
        currentBlog.headhtml=utility.GetPostData(request,"headhtml")
        currentBlog.footerhtml=utility.GetPostData(request,"footerhtml")
  
        currentBlog.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/config/blog.html",locals())


