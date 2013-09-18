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

        myModules=["newuserlist","hotarticlelist","newarticlelist"]
        moduleParams={}
        for myModule in myModules:
            moduleParams.setdefault(myModule,{})

        moduleList=modules.GetModuleList(moduleParams)

        channels=Channel.objects.filter(parent_id=0)
        articleList={}
        from UUBlog.apps.blog.views import viewblock
        for channel in channels:
            retValue=[]
            blockChannelPic=viewblock.GetBlockValue("channel_%s_pic" %channel.id,1)
            blockChannelList=viewblock.GetBlockValue("channel_%s" %channel.id,5)

            retValue.append(blockChannelPic)
            retValue.append(blockChannelList)

            articleList.setdefault(channel,retValue)

        self.template_name="blog/index.html"

        return locals()

