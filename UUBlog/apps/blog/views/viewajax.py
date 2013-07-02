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
from UUBlog.common import pub,utility
from django.utils import simplejson as json

@login_required()
def listenchannel(request,cid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    
    currentBlog=userInfos["currentblog"]

    channelId=pub.GetGetData(request,"channelid")
    currentBlog.listenchannels+="%s," %channelId
    currentBlog.save()

   
    retjson=json.dumps({"code":0})
    return HttpResponse(retjson)

@login_required()
def followblog(request,bid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    
    currentBlog=userInfos["currentblog"]
    followBlogId=pub.GetGetData(request,"blogid")

    follow=Follow()
    follow.blog_id=currentBlog.id
    follow.follow_blog_id=followBlogId
    follow.save()

    followBlog=Blog.objects.get(id=followBlogId)
    followBlog.follows+=1
    followBlog.save()
   
    retjson=json.dumps({"code":0})
    return HttpResponse(retjson)


@login_required()
def suggestblog(request,bid=-1):
    userInfos=viewaccounts.UsersMeta(request,-1)
    
    currentBlog=userInfos["currentblog"]
    suggestBlogId=pub.GetGetData(request,"blogid")

    suggest=Suggest()
    suggest.blog_id=currentBlog.id
    suggest.suggest_blog_id=suggestBlogId
    suggest.save()

    suggestBlog=Blog.objects.get(id=suggestBlogId)
    suggestBlog.suggestes+=1
    suggestBlog.lastsuggesttime=datetime.datetime.now()
    suggestBlog.save()
   
    retjson=json.dumps({"code":0})
    return HttpResponse(retjson)




#def channel(request,cid=-1):
#    userInfos=viewaccounts.UsersMeta(request,1)

#    myModules=["newuserlist","hotarticlelist","newarticlelist"]
#    moduleParams={}
#    for myModule in myModules:
#        moduleParams.setdefault(myModule,{})

#    moduleList=modules.GetModuleList(moduleParams)

#    articleList=Article.objects.order_by("-createtime").filter(channel1_id=cid)


#    channelList=Channel.objects.all()
#    currentChannel=Channel.objects.get(id=cid)
#    childrenChannel=Channel.objects.filter(parent_id=cid)

#    return pub.my_render_to_response(request,"channel.html",locals())

#def test(request):
#    return pub.my_render_to_response(request,"test.html",locals())