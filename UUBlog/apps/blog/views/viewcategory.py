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


categoryroot="/%d/pub/category/"

def GetCategoryList(uid=-1):
    if uid>0:
        categoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)
    else:
        categoryList=Category.objects.order_by("-sortnum").all()

    return categoryList

@login_required()
def add(request):
    uid=int(-1)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    name=pub.GetPostData(request,"name")
    sortnum=pub.GetPostData(request,"sortnum")

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
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    name=pub.GetPostData(request,"name")
    sortnum=pub.GetPostData(request,"sortnum")

    if request.POST.has_key('ok'):
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.name=name
        categoryInfo.sortnum=sortnum
        categoryInfo.save()

        return HttpResponseRedirect(categoryroot %currentUser.id)

    else:
        categoryInfo=Category.objects.get(id=cid)
        return pub.my_render_to_response(request,"blog/pub/category.html",locals())

@login_required()
def delete(request,uid,cid=-1):
    uid=int(-1)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    #articleList=Article.objects.filter(user_id=1)
    categoryInfo=Category.objects.get(id=cid)
    categoryInfo.delete()

    return HttpResponseRedirect(categoryroot %currentUser.id)

@login_required()
def index(request,uid,cid=-1):
    uid=int(-1)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]
   
    categoryList=GetCategoryList(currentUser.id)
    
    if request.POST.has_key('ok'):
        return add(request)
    else:
        return pub.my_render_to_response(request,"blog/pub/category.html",locals())
    