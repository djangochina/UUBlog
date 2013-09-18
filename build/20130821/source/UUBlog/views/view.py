#-*- coding:utf-8 -*-
import uuid
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

from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.common import pub,utility

from UUBlog.models import *
from UUBlog.uu.ubaseblog import *



#用户博客首页
class IndexView(UBaseBlogView):

    def GetContext(self, **kwargs):

        myWidgetList=self.GetMyWidgetList()

        postList=self.GetPostList()

        pageIndex=int(self.GetGetData("page",1))

        postList=pub.GetPagedObject(postList,pageIndex,self.GetOption("pagesize_index",10))

        pageObject=postList

        #更新博客访客
        #self.AddVisit(uid)

        self.SetTemplateName("index_normal")

        return locals()

#列表浏览
class ListView(UBaseBlogView):

    def GetContext(self, **kwargs):
        myWidgetList=self.GetMyWidgetList()

        cid=int(self.GetDicData(kwargs,"cid",0))
        tid=int(self.GetDicData(kwargs,"tid",0))
        pageIndex=int(self.GetGetData("page",1))

        listTemplateType="normal"        

        postList=Post.objects.order_by("-createtime").filter(status=1)
        if cid>0:
            postList=postList.filter(category_id=cid)
            listTemplateType="cat"
        if tid>0:
            listTemplateType="tag"
            pass


        postList=pub.GetPagedObject(postList,pageIndex,self.GetOption("pagesize_user",10))

        pageObject=postList

        self.SetTemplateName("list_"+listTemplateType)

        return locals()

#文章页面
class PostView(UBaseBlogView):

    def GetContext(self, **kwargs):
        pid=int(kwargs.get("pid",0))

        myWidgetList=self.GetMyWidgetList()
    
        postInfo=Post.objects.get(id=pid)

        #更新文章浏览量
        postInfo.views+=1
        postInfo.save()

        hookList=self.GetHookList("post_BeforShow")
        for hook in hookList:
            if callable(hook):
                postInfo=hook(postInfo)
        

        commentList=Comment.objects.filter(post_id=pid)

        self.SetTemplateName("post_normal")

        return locals()

    def PostContext(self, **kwargs):
        aid=int(kwargs.get("aid",0))

        if self.HasPostData("ok"):
            username = self.GetPostData('username')
            content = self.GetPostData('content')

            articleInfo=Article.objects.get(id=aid)
            comment=Comment()
            comment.article=articleInfo
            comment.content=content
            comment.user_id=self.currentUserProfile.user_id
            comment.username=username
            comment.createtime=datetime.datetime.now()
            comment.save()

            articleInfo.comments+=1
            articleInfo.save()

#文章页面
class PageView(UBaseBlogView):

    def GetContext(self, **kwargs):
        pid=int(kwargs.get("pid",0))

        myWidgetList=self.GetMyWidgetList()
    
        pageInfo=Page.objects.get(id=pid)

        #更新文章浏览量
        pageInfo.views+=1
        pageInfo.save()

      
        

        #commentList=Comment.objects.filter(obj_id=pid)

        self.SetTemplateName("page_normal")

        return locals()

    def PostContext(self, **kwargs):
        aid=int(kwargs.get("aid",0))

        if self.HasPostData("ok"):
            username = self.GetPostData('username')
            content = self.GetPostData('content')

            articleInfo=Article.objects.get(id=aid)
            comment=Comment()
            comment.article=articleInfo
            comment.content=content
            comment.user_id=self.currentUserProfile.user_id
            comment.username=username
            comment.createtime=datetime.datetime.now()
            comment.save()

            articleInfo.comments+=1
            articleInfo.save()           