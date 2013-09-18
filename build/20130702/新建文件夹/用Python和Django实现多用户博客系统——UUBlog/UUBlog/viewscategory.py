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
from UUBlog.models import Category, Article

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
import common
import utility

categoryroot="/%d/pub/category/"

@login_required()
def add(request):
    uid=int(-1)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    name=utility.GetPostData(request,"name")
    sortnum=utility.GetPostData(request,"sortnum")

    if request.POST.has_key('ok'):
        categoryInfo=Category()
        categoryInfo.name=name
        categoryInfo.sortnum=sortnum
        categoryInfo.user_id=currentUser.id
        categoryInfo.save()

    return HttpResponseRedirect(categoryroot %currentUser.id)

@login_required()
def edit(request,uid,cid):
    uid=int(-1)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    name=utility.GetPostData(request,"name")
    sortnum=utility.GetPostData(request,"sortnum")

    if request.POST.has_key('ok'):
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.name=name
        categoryInfo.sortnum=sortnum
        categoryInfo.save()

        return HttpResponseRedirect(categoryroot %currentUser.id)

    else:
        categoryInfo=Category.objects.get(id=cid)
        return utility.my_render_to_response(request,"pub/category.html",locals())

@login_required()
def delete(request,uid,cid=-1):
    uid=int(-1)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    #articleList=Article.objects.filter(user_id=1)
    categoryInfo=Category.objects.get(id=cid)
    categoryInfo.delete()

    return HttpResponseRedirect(categoryroot %currentUser.id)

@login_required()
def index(request,uid,cid=-1):
    uid=int(-1)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]
   
    categoryList=common.categoryList(currentUser.id)
    
    if request.POST.has_key('ok'):
        return add(request)
    else:
        return utility.my_render_to_response(request,"pub/category.html",locals())
    