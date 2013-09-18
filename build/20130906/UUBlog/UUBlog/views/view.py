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

from UUBlog.common import pub,utility

from UUBlog.models import *
from UUBlog.uu.ubaseuser import *



#用户博客首页
class IndexView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(IndexView, self).GetContext(**kwargs)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("index_pagesize",20)

        postList=self.GetPostList(status=1)
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList
       
        self.sidebar=self.GetOption("index_sidebar","normal")
        self.templateName="index_"+self.GetOption("index_template","normal")

        self.SetTemplateAndSidebar()

        return locals()

#列表浏览
class ListView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(ListView, self).GetContext(**kwargs)

        cid= utility.ToInt(utility.GetDicData(kwargs,"cid"),0)
        tid= utility.ToInt(utility.GetDicData(kwargs,"tid"),0)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=20

        postList=self.GetPostList(status=1)
        if cid>0:
            pageSize=self.GetOption("cat_pagesize",20)
            postList=postList.filter(category_id=cid)

            catInfo=Category.objects.get(id=cid)

            self.sidebar=catInfo.sidebar
            self.templateName="cat_"+catInfo.template
        if tid>0:
            #pageSize=self.GetOption("tag_pagesize",10)
            #postList=postList.filter(category_id=cid)
            #self.sidebar=catInfo.sidebar
            #self.templateName="tag_"+catInfo.template

            pass

        
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList

        self.SetTemplateAndSidebar()
        return locals()

#列表浏览
class SearchView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(SearchView, self).GetContext(**kwargs)


        word=self.GetGetData("word")
        
        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("search_pagesize",20)

        postList=self.GetPostList(status=1,title__icontains=word)
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList

        self.sidebar=self.GetOption("search_sidebar","normal")
        self.templateName="search_"+self.GetOption("search_template","normal")

        self.SetTemplateAndSidebar()
        return locals()

#文章页面
class PostView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(PostView, self).GetContext(**kwargs)

        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)
    
        postInfo=self.GetPost(pid)

        #更新文章浏览量
        postInfo.views+=1
        postInfo.save()

        hookList=self.GetHookList("post_BeforShow")
        for hook in hookList:
            if callable(hook):
                postInfo=hook(postInfo)
        
        objInfo=postInfo
        commentList=self.GetCommentList(obj_id=pid)

        comment_paging = self.GetOption("comment_paging","True")
        if comment_paging=="True":
            pageIndex=utility.ToInt(self.GetGetData("page"),1)
            pageSize=self.GetOption("comment_pagesize",20)
        
            commentList=pub.GetPagedObject(commentList,pageIndex,pageSize)
            pageObject=commentList
            

        self.sidebar=postInfo.sidebar
        self.templateName="post_"+postInfo.template
        
        self.SetTemplateAndSidebar()
        return locals()

    def PostContext(self, **kwargs):
        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

        if self.HasPostData("ok") and pid>0:
            postInfo=Post.objects.get(id=pid)

            username = self.GetPostData('username')
            email = self.GetPostData('email')
            content = self.GetPostData('content')
            
            commentInfo=Comment()
            commentInfo.obj_id=pid
            commentInfo.title=postInfo.title
            commentInfo.content=content
            commentInfo.createtime=datetime.datetime.now()
            commentInfo.user_id=0
            commentInfo.username=username
            commentInfo.email=""

            commentInfo.save()

            postInfo.comments+=1
            postInfo.save()

#文章页面
class PageView(UBaseUserView):
    
    def GetContext(self, **kwargs):
        super(PageView, self).GetContext(**kwargs)

        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

    
        pageInfo=self.GetPage(pid)

        #更新文章浏览量
        pageInfo.views+=1
        pageInfo.save()

        
        objInfo=pageInfo
        commentList=self.GetCommentList(obj_id=pid)

        comment_paging = self.GetOption("comment_paging","True")
        if comment_paging=="True":
            pageIndex=utility.ToInt(self.GetGetData("page"),1)
            pageSize=self.GetOption("comment_pagesize",20)
        
            commentList=pub.GetPagedObject(commentList,pageIndex,pageSize)
            pageObject=commentList


        self.sidebar=pageInfo.sidebar
        self.templateName="page_"+pageInfo.template

        self.SetTemplateAndSidebar()
        return locals()

    def PostContext(self, **kwargs):
        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

        if self.HasPostData("ok") and pid>0:
            pageInfo=Page.objects.get(id=pid)

            username = self.GetPostData('username')
            email = self.GetPostData('email')
            content = self.GetPostData('content')
            
            commentInfo=Comment()
            commentInfo.obj_id=pid
            commentInfo.title=pageInfo.title
            commentInfo.content=content
            commentInfo.createtime=datetime.datetime.now()
            commentInfo.user_id=0
            commentInfo.username=username
            commentInfo.email=""

            commentInfo.save()

            pageInfo.comments+=1
            pageInfo.save()    
            
            
            
            
   