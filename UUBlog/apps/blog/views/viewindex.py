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


def index(request):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    channels=Channel.objects.filter(parent_id=0)
    articleList={}
    for channel in channels:
        retValue=pub.getModelResult(Article,"-createtime",channel1_id=channel.id,status=1,ishome=1)
        #retValue=Article.objects.order_by("-createtime").filter(channel1_id=channelId)
        articleList.setdefault(channel,retValue)

    return pub.my_render_to_response(request,"blog/index.html",locals())


def test(request):
    return pub.my_render_to_response(request,"test.html",locals())