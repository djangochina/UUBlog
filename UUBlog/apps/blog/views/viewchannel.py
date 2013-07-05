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
from UUBlog.apps.blog.views.baseblogview import *

class IndexView(UBaseBlogView):


    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
        c2id=int(kwargs.get("c2id",0))

        channelList=Channel.objects.filter(parent_id=0)
        parentChannel=Channel.objects.get(id=cid)
        childrenChannel=Channel.objects.filter(parent_id=cid)
        listenChannelId=cid

        try:
            childChannel=Channel.objects.get(id=c2id)
            listenChannelId=c2id

            articleList=Article.objects.order_by("-createtime").filter(channel2_id=c2id)

        except:
            childChannel=None
            articleList=Article.objects.order_by("-createtime").filter(channel1_id=cid)
        
    

        myChannelList=[]
        hasListened=False

        if self.currentBlog:
            dot=self.currentBlog.listenchannels.find("%s," %cid)
            hasListened=True if dot>-1 else False

            myChannelArray=self.currentBlog.listenchannels.split(",")
            for tempCId in myChannelArray:
                if tempCId!="":
                    myChannelList.append(Channel.objects.get(id=tempCId))

       

        self.template_name="blog/channel.html"

        return locals()

def popular(request,cid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    articleList=Article.objects.order_by("-createtime").filter(channel1_id=cid)


    channelList=Channel.objects.filter(parent_id=0)
    channelListPopular=Channel.objects.all()

    return pub.my_render_to_response(request,"blog/channelpopular.html",locals())

def my(request,cid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)

    myModules=["newuserlist","hotarticlelist","newarticlelist"]
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{})

    moduleList=modules.GetModuleList(moduleParams)

    articleList=Article.objects.order_by("-createtime").filter(channel1_id=cid)


    channelList=Channel.objects.filter(parent_id=0)
    channelListPopular=Channel.objects.all()

    return pub.my_render_to_response(request,"blog/channelpopular.html",locals())



