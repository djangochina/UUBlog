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

from UUBlog.models import Category, Article

from django.views.generic.base import TemplateView

import common


def my_render_to_response(request,templateName,locals):
    return render_to_response(templateName,locals,context_instance=RequestContext(request))

def GetPostData(request,key,default=""):
    if request.POST.has_key(key):
        return request.POST[key]
    return default

def login(request):
    return True

def logout(request):
    return False

def home(request):
    viewsTopArticles=common.viewsTopArticles()
    remarkTopArticles=common.remarkTopArticles()
    newTopArticles=common.newTopArticles()
    categoryList=common.categoryList()

    articleList=Article.objects.order_by("-createtime").all()

    return my_render_to_response(request,"home.html",locals())
    #return HttpResponse(html)

def show(request,aid):
    viewsTopArticles=common.viewsTopArticles()
    remarkTopArticles=common.remarkTopArticles()
    newTopArticles=common.newTopArticles()
    categoryList=common.categoryList()

    articleInfo=Article.objects.get(id=aid)
    title=articleInfo.title
    content=articleInfo.content
    articleInfo.views+=1
    if not articleInfo.createtime:
        articleInfo.createtime=datetime.datetime.now()

    articleInfo.save()

    return my_render_to_response(request,"articleshow.html",locals())

def add(request):
    viewsTopArticles=common.viewsTopArticles()
    remarkTopArticles=common.remarkTopArticles()
    newTopArticles=common.newTopArticles()
    categoryList=common.categoryList()

    if request.POST.has_key('ok'):
        category=Category.objects.get(id=GetPostData(request,'category'))
        title = GetPostData(request,'title')
        pic = GetPostData(request,'pic')
        tags=GetPostData(request,'tags')
        summary=GetPostData(request,'summary')
        content = GetPostData(request,'content')
        
        if len(summary)==0:
            summary=summary[1:80] if len(summary)>80 else summary

        articleInfo = Article(category=category,
                              title = title,
                              pic="",
                              tags=tags,
                              summary=summary,
                              content = content,
                              createtime=datetime.datetime.now(),
                              views=0,
                              comments=0,
                              goods=0,
                              bads=0,
                              status=1,
                              user_id=1,
                              user_name="admin")
        articleInfo.save()

        return HttpResponseRedirect('/')
    else:
        return my_render_to_response(request,"addarticle.html",locals())
    


def edit(request,aid):
    viewsTopArticles=common.viewsTopArticles()
    remarkTopArticles=common.remarkTopArticles()
    newTopArticles=common.newTopArticles()
    categoryList=common.categoryList()


    if request.POST.has_key('ok'):
        articleInfo=Article.objects.get(id=aid)
        
        articleInfo.category=Category.objects.get(id=GetPostData(request,'category'))
        articleInfo.title = GetPostData(request,'title')
        articleInfo.pic = GetPostData(request,'pic')
        articleInfo.tags=GetPostData(request,'tags')
        articleInfo.summary=GetPostData(request,'summary')
        articleInfo.content = GetPostData(request,'content')

        articleInfo.save()

        return HttpResponseRedirect('/')
    else:
        articleInfo=Article.objects.get(id=aid)
        title=articleInfo.title
        content=articleInfo.content
        return my_render_to_response(request,"editarticle.html",locals())


def category(request,action="",cid=-1):
    viewsTopArticles=common.viewsTopArticles()
    remarkTopArticles=common.remarkTopArticles()
    newTopArticles=common.newTopArticles()
    categoryList=common.categoryList()
    

    if request.POST.has_key('ok'):
        name = request.POST['name']
        if cid!=-1:
            categoryInfo=Category(name=name)
        else:
            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
        categoryInfo.save()

        return HttpResponseRedirect('/')
    else:

        return my_render_to_response(request,"category.html",locals())

def action(request,action):
    if action=="edit":
        aaa=1

class BaseRequest:
    def GetPost(self,article):
            title = article['title']
            content = article['content']
            tags = article['tags']
            times = time.time()
            cate_id = int(request.POST['category'])

def aaa(request):
    if not editId:
        if request.POST.has_key('ok'):
            caption = request.POST['caption']
            shortContent = request.POST['description']
            content = request.POST['content']
            tags = request.POST['tags']
            times = time.time()
            cate_id = int(request.POST['category'])
            if caption and shortContent:
                addArticle = Models.Article(caption = caption,shortContent = shortContent,
                            content = content,tags = tags,times = times,degree = 1,
                            cate_id = cate_id)
                addArticle.save()
                return HttpResponseRedirect('/addArticle/')
    else:#编辑文章
        article = Models.Article.objects.filter(id = int(editId)).values('cate_id','tags',
                'caption','content','shortContent')
        caption =  article[0]['caption']
        content = article[0]['content']
        cateId = article[0]['cate_id']
        tags = article[0]['tags']
        description = article[0]['shortContent']
        if request.POST.has_key('ok'):
            caption = request.POST['caption']
            shortContent = request.POST['description']
            content = request.POST['content']
            tags = request.POST['tags']
            times = time.time()
            cate_id = int(request.POST['category'])
            if caption and shortContent:
                Models.Article.objects.filter(id = editId).update(caption = caption,
                            shortContent = shortContent,content = content,tags = tags,
                            cate = cate_id)
                return HttpResponseRedirect('/addArticle/?action='+editId)
    return render_to_response('admin/addArticle.html',locals())


class MyBaseView(TemplateView):

    def __init__(self,request):
        self.request=request

    def my_render_to_response(self,templateName,locals):
        return render_to_response(templateName,locals,context_instance=RequestContext(self.request))

    def home(self):
        adf=5

    def add(self):
        aaa=0

    def update(self):
        asdfasfd=2

    def delete(self,id):
        aaa=""

    def getPostData(self,key):
        if self.request.POST.has_key(key):
            return self.request.POST[key]
        return ''
    def hasPostData(self,key):
        return self.request.POST.has_key(key)

class ArticleView(MyBaseView):

    def __init__(self, request):
        return super(ArticleView, self).__init__(request)

    def add(self):

        if self.hasPostData('ok'):

                title =self.getPostData('title')
                content = self.getPostData('content')

                category=Category.objects.get(id=1)
                createtime=datetime.datetime.now()
                views=0

                addArticle = Article(title = title,content = content,category=category,createtime=createtime,views=views)
                addArticle.save()

                return HttpResponseRedirect('/')

        return MyBaseView.my_render_to_response(self,request,"addarticle.html",locals())








