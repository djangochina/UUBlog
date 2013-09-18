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

from UUBlog.models import Category, Article,Blog,Channel

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
import common
import utility
import modules


def index(request):
    userInfos=common.Users(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    channelIds={1,2,3}
    #channelIds.add()
    articleList={}
    for channelId in channelIds:
        channel=Channel.objects.get(id=channelId)
        if channel:
            retValue=Article.objects.order_by("-createtime").filter(channel1_id=channelId)
            articleList.setdefault(channel,retValue)

    return utility.my_render_to_response(request,"index.html",locals())

def channel(request,cid=-1):
    userInfos=common.Users(request,1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    articleList=Article.objects.order_by("-createtime").filter(channel1_id=cid)


    channelList=Channel.objects.all()
    currentChannel=Channel.objects.get(id=cid)
    childrenChannel=Channel.objects.filter(parent_id=cid)

    return utility.my_render_to_response(request,"channel.html",locals())

def test(request):
    return utility.my_render_to_response(request,"test.html",locals())