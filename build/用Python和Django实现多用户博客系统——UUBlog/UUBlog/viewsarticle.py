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

from UUBlog.models import Category, Article,Comment,Channel
import common
import modules
import utility

#未分类和草稿不计入统计

#博客首页
def home(request,uid):
    uid=int(uid)
    userInfos=common.Users(request,uid)
    
    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    #更新用户文章总数
    guestBlog.todayviews+=1
    guestBlog.totalviews+=1
    guestBlog.save()

    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(status=1)
    
    return utility.my_render_to_response(request,"Skins/"+guestBlog.template+"/home.html",locals())


#文章页面
def show(request,uid=-1,aid=-1,*arg,**kwarg):
    uid=int(uid)
    userInfos=common.Users(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)
    

    articleInfo=Article.objects.get(id=aid)

    

    if request.POST.has_key('ok'):
        username = utility.GetPostData(request,'username')
        content = utility.GetPostData(request,'content')

        comment=Comment()
        comment.article=articleInfo
        comment.content=content
        comment.user_id=userInfos["currentuser"].id
        comment.username=username
        comment.createtime=datetime.datetime.now()
        comment.save()

        articleInfo.comments+=1

        guestBlog=userInfos["guestblog"]
        guestBlog.comments+=1
        guestBlog.save()

    commentList=Comment.objects.filter(article_id=aid)

    #更新文章浏览量
    articleInfo.views+=1
    articleInfo.save()

    return utility.my_render_to_response(request,"Skins/"+guestBlog.template+"/show.html",locals())

#分类浏览
def category(request,uid,cid):
    uid=int(uid)
    userInfos=common.Users(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    currentCategory=Category.objects.get(id=cid)

    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

    return utility.my_render_to_response(request,"Skins/"+guestBlog.template+"/home.html",locals())

#tags浏览
def tags(request,uid,cid):
    uid=int(uid)
    userInfos=common.Users(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

    return utility.my_render_to_response(request,"Skins/"+guestBlog.template+"/home.html",locals())

@login_required()
def list(request,uid):
    uid=int(uid)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id)

    return utility.my_render_to_response(request,"pub/articlelist.html",locals())

@login_required()
def listdraft(request,uid):
    uid=int(uid)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id).filter(status=0)
    return utility.my_render_to_response(request,"pub/articlelist.html",locals())


@login_required()
def listcategory(request,uid,cid=-1):
    uid=int(uid)
    cid=int(cid)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id).filter(category_id=cid)

    return utility.my_render_to_response(request,"pub/articlelist.html",locals())


@login_required()
def add(request,*arg,**kwarg):
    uid=int(-1)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)
    channelList=Channel.objects.all()

    if request.POST.has_key('ok'):
        channel1Id=int(utility.GetPostData(request,'channel1',0))
        channel2Id=int(utility.GetPostData(request,'channel1',0))
        cateId=int(utility.GetPostData(request,'category'))
        category=Category.objects.get(id=utility.GetPostData(request,'category'))
        
        title = utility.GetPostData(request,'title')
        pic = utility.GetPostData(request,'pic')
        tags=utility.GetPostData(request,'tags')
        summary=utility.GetPostData(request,'summary')
        content = utility.GetPostData(request,'content')
        status = utility.GetPostData(request,'status')
        
        ishome=utility.GetPostData(request,'ishome')
        isrecommend = utility.GetPostData(request,'isrecommend')
        istop = utility.GetPostData(request,'istop')
        isoriginal=utility.GetPostData(request,'isoriginal')
        cancomment = utility.GetPostData(request,'cancomment')
        password = utility.GetPostData(request,'password')

        if summary=="":
            tempContent=utility.RemoveTags(content)
            summary=tempContent[0:200] if len(tempContent)>200 else tempContent
        else:
            summary=utility.RemoveTags(summary)

        articleInfo=Article(category=category)

        articleInfo.channel1_id=channel1Id
        articleInfo.channel2_id=channel2Id
        articleInfo.category=category
        articleInfo.title = title
        articleInfo.pic=pic
        articleInfo.tags=tags
        articleInfo.summary=summary
        articleInfo.content = content
        articleInfo.createtime=datetime.datetime.now()
        articleInfo.views=0
        articleInfo.comments=0
        articleInfo.goods=0
        articleInfo.bads=0
        articleInfo.status=1 if status else 0
        articleInfo.user_id=currentUser.id
        articleInfo.username=currentUser.username

        articleInfo.ishome=1 if ishome else 0
        articleInfo.isrecommend=1 if isrecommend else 0
        articleInfo.istop=1 if istop else 0
        articleInfo.isoriginal=1 if isoriginal else 0
        articleInfo.cancomment=1 if cancomment else 0
        articleInfo.password=password

        articleInfo.save()

        #更新分类统计信息 不是默认分类并且是发布的文章
        if category.id !=1 and status:
            category.articles+=1
            category.save()

        #更新用户文章统计信息
        currentBlog=userInfos["currentblog"]
        currentBlog.articles+=1
        currentBlog.save()

        if channel1Id>0:
            channel1=Channel.objects.get(id=channel1Id)
            channel1.articles+=1
            channel1.save()
        if channel2Id>0:
            channel2=Channel.objects.get(id=channel2Id)
            channel2.articles+=1
            channel2.save()

        return HttpResponseRedirect('/%d/' %request.user.id)
    else:
        
        articleInfo=Article()

        return utility.my_render_to_response(request,"pub/articleedit.html",locals())

@login_required()
def edit(request,uid,aid):
    uid=int(uid)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)
    channelList=Channel.objects.all()

    articleInfo=Article.objects.get(id=aid)
    oldCategory=articleInfo.category
    oldStatus=articleInfo.status

    if request.POST.has_key('ok'):
        channel1Id=int(utility.GetPostData(request,'channel1',0))
        channel2Id=int(utility.GetPostData(request,'channel2',0))
        cateId=int(utility.GetPostData(request,'category'))
        category=Category.objects.get(id=utility.GetPostData(request,'category'))

        title = utility.GetPostData(request,'title')
        pic = utility.GetPostData(request,'pic')
        tags=utility.GetPostData(request,'tags')
        summary=utility.GetPostData(request,'summary')
        content = utility.GetPostData(request,'content')
        status = utility.GetPostData(request,'status')

        ishome=utility.GetPostData(request,'ishome')
        isrecommend = utility.GetPostData(request,'isrecommend')
        istop = utility.GetPostData(request,'istop')
        isoriginal=utility.GetPostData(request,'isoriginal')
        cancomment = utility.GetPostData(request,'cancomment')
        password = utility.GetPostData(request,'password')

        if summary=="":
            tempContent=utility.RemoveTags(content)
            summary=tempContent[0:200] if len(tempContent)>200 else tempContent
        else:
            summary=utility.RemoveTags(summary)

        articleInfo.channel1_id=channel1Id
        articleInfo.channel2_id=channel2Id
        articleInfo.category=category
        articleInfo.title = title
        articleInfo.pic=pic
        articleInfo.tags=tags
        articleInfo.summary=summary
        articleInfo.content = content
        #articleInfo.createtime=datetime.datetime.now()
        #articleInfo.views=0
        #articleInfo.comments=0
        #articleInfo.goods=0
        #articleInfo.bads=0
        articleInfo.status=1 if status else 0
        #articleInfo.user_id=request.user.id
        #articleInfo.username=request.user.username

        articleInfo.ishome=1 if ishome else 0
        articleInfo.isrecommend=1 if isrecommend else 0
        articleInfo.istop=1 if istop else 0
        articleInfo.isoriginal=1 if isoriginal else 0
        articleInfo.cancomment=1 if cancomment else 0
        articleInfo.password=password

        if oldCategory != category:
            #不是未分类，并且已经发布
            if category.id !=1 and status:
                category.articles+=1
                category.save()
            #不是未分类，并且已经是草稿
            if oldCategory.id!=1 and oldStatus:
                oldCategory.articles=oldCategory.articles-1 if oldCategory.articles>1 else 0
                oldCategory.save()
        else:
            if not status:
                category.articles-=1
                category.save()

        articleInfo.save()

        return HttpResponseRedirect('/%d/' %request.user.id)
    else:
        return utility.my_render_to_response(request,"pub/articleedit.html",locals())

@login_required()
def delete(request,aid,uid=-1):
    uid=int(uid)
    userInfos=common.Users(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=common.categoryList(currentUser.id)

    articleInfo=Article.objects.get(id=aid)
    
    if articleInfo.status:
        category=articleInfo.category
        #更新分类统计信息
        if category.id !=1:
            category.articles-=1
            category.save()

        #更新用户统计信息
        blog=userInfos[2]
        blog.articles-=1
        blog.save()

    articleInfo.delete()

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id)
    
    return HttpResponseRedirect('/pub/article/list/')


