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

def createBlog(user):
  
    blog=Blog()
    blog.id=user.id
    blog.title=user.username+"的博客".decode("utf-8")
    blog.description="欢迎来".decode("utf-8")+user.username+"的博客".decode("utf-8")
    blog.keywords=user.username
    blog.modules="profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist"
    blog.template="default"
    blog.createtime=datetime.datetime.now()
    blog.save()

class IndexView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        aid=int(kwargs.get("aid",-1))
        
        block2List=Block.objects.filter(type=2).order_by("-createtime")

        self.template_name="blog/block.html"

        return locals()
    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            aid=self.GetPostData("aid")
            block2Ids=self.GetRequestListData("block2")

            for block2Id in block2Ids:
                articleInfo=Article.objects.get(id=aid)

                block2Info=Block2()
                block2Info.block_id=block2Id
                block2Info.title=articleInfo.title
                block2Info.titlestyle=articleInfo.titlestyle
                block2Info.titlepic=articleInfo.titlepic
                block2Info.createtime=datetime.datetime.now();
                block2Info.summary=articleInfo.summary
                block2Info.titleurl="/%s/show/%s" %(articleInfo.user_id,articleInfo.id)
                block2Info.save();
        
        return locals()





def GetBlockValue(blockName,count=10,returnModelIf1=True):
    ret={}

    blockInfo=None
    values=None

    try:
        blockInfo=Block.objects.get(name=blockName)
    except:
        pass

    if blockInfo:
        
        if blockInfo.type==1:
            values=Block1.objects.filter(block_id=blockInfo.id).order_by("-createtime")[0:count]

        elif blockInfo.type==2:
            values=Block2.objects.filter(block_id=blockInfo.id).order_by("-createtime")[0:count]

    if values and count==1 and returnModelIf1:
        return values[0]
    return values


