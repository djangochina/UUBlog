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
from UUBlog.apps.blog.views import viewcategory,baseblogview
from UUBlog.apps.blog.views.baseblogview import *
from UUBlog.apps.blog import modules
from UUBlog.core.ubasetemplateView import UBaseTemplateView

#未分类和草稿不计入统计

#博客首页
class Home(UBaseBlogView):

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        moduleList=self.GetBlogModuleList(uid)
        navigateCategoryList=self.GetNavigateCategoryList(uid)
        followBlogIds=self.GetFollowBlogIds(uid)
        suggestBlogIds=self.GetSuggestBlogIds(uid)
        articleList=self.GetArticleList(uid)

        #更新用户文章总数
        self.guestBlog.todayviews+=1
        self.guestBlog.totalviews+=1
        self.guestBlog.save()
    
        self.AddVisit(uid)

        self.template_name="blog/skins/"+self.guestBlog.template+"/home.html"

        return locals()


#文章页面
class Show(UBaseBlogView):

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        aid=int(kwargs.get("aid",0))

        moduleList=self.GetBlogModuleList(uid)
        navigateCategoryList=self.GetNavigateCategoryList(uid)
        followBlogIds=self.GetFollowBlogIds(uid)
        suggestBlogIds=self.GetSuggestBlogIds(uid)
        articleList=self.GetArticleList(uid)

        #更新用户文章总数
        self.guestBlog.todayviews+=1
        self.guestBlog.totalviews+=1
        self.guestBlog.save()
    
        self.AddVisit(uid)
        
    
        articleInfo=Article.objects.get(id=aid)

        #更新文章浏览量
        articleInfo.views+=1
        articleInfo.save()

        
        if self.HasPostData("ok"):
            username = self.GetPostData(request,'username')
            content = self.GetPostData(request,'content')

            comment=Comment()
            comment.article=articleInfo
            comment.content=content
            comment.user_id=self.currentUserProfile.user_id
            comment.username=username
            comment.createtime=datetime.datetime.now()
            comment.save()

            articleInfo.comments+=1

            self.guestBlog.comments+=1
            self.guestBlog.save()

        commentList=Comment.objects.filter(article_id=aid)


        self.template_name="blog/skins/"+self.guestBlog.template+"/show.html"

        return locals()



def home(request,uid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    
    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    navigateCategoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)

    #更新用户文章总数
    guestBlog.todayviews+=1
    guestBlog.totalviews+=1
    guestBlog.save()

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    suggestBlogIds=[]
    if currentBlog:
        suggestList=Suggest.objects.filter(blog_id=currentBlog.id)
        for suggest in suggestList:
            suggestBlogIds.append(suggest.suggest_blog_id)
    
    if currentBlog and currentBlog.id!=guestBlog.id:
        visit=Visit.objects.filter(blog_id=currentBlog.id,visit_blog_id=guestBlog.id)
        if not visit:
            visit=Visit()
            visit.blog_id=currentBlog.id
            visit.visit_blog_id=guestBlog.id
            visit.lastvisittime=datetime.datetime.now()
            visit.save()
       

    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(status=1)
    
    return pub.my_render_to_response(request,"blog/skins/"+guestBlog.template+"/home.html",locals())


#文章页面
def show(request,uid=-1,aid=-1,*arg,**kwarg):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)
    
    navigateCategoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)

    articleInfo=Article.objects.get(id=aid)

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    suggestBlogIds=[]
    if currentBlog:
        suggestList=Suggest.objects.filter(blog_id=currentBlog.id)
        for suggest in suggestList:
            suggestBlogIds.append(suggest.suggest_blog_id)


    if request.POST.has_key('ok'):
        username = pub.GetPostData(request,'username')
        content = pub.GetPostData(request,'content')

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

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/skins/"+guestBlog.template+"/show.html",locals())

#分类浏览
def category(request,uid,cid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    currentCategory=Category.objects.get(id=cid)

    navigateCategoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)
    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/skins/"+guestBlog.template+"/home.html",locals())

#tags浏览
def tags(request,uid,cid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)

    guestBlog=userInfos["guestblog"]

    myModules=guestBlog.modules.split(",")
    moduleParams={}
    for myModule in myModules:
        moduleParams.setdefault(myModule,{"uid":uid})

    moduleList=modules.GetModuleList(moduleParams)

    articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

    currentBlog=userInfos["currentblog"]
    followBlogIds=[]
    if currentBlog:
        followList=Follow.objects.filter(blog_id=currentBlog.id)
        for follow in followList:
            followBlogIds.append(follow.follow_blog_id)

    return pub.my_render_to_response(request,"blog/skins/"+guestBlog.template+"/home.html",locals())

@login_required()
def list(request,uid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id)

    return pub.my_render_to_response(request,"blog/pub/articlelist.html",locals())

@login_required()
def listdraft(request,uid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id).filter(status=0)
    return pub.my_render_to_response(request,"blog/pub/articlelist.html",locals())


@login_required()
def listcategory(request,uid,cid=-1):
    uid=int(uid)
    cid=int(cid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)

    articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id).filter(category_id=cid)

    return pub.my_render_to_response(request,"blog/pub/articlelist.html",locals())


@login_required()
def add(request,*arg,**kwarg):
    uid=int(-1)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)
    channelList=Channel.objects.filter(parent_id=0)

    if request.POST.has_key('ok'):
        channel1Id=int(pub.GetPostData(request,'channel1',0))
        channel2Id=int(pub.GetPostData(request,'channel1',0))
        cateId=int(pub.GetPostData(request,'category'))
        category=Category.objects.get(id=pub.GetPostData(request,'category'))
        
        title = pub.GetPostData(request,'title')
        pic = pub.GetPostData(request,'pic')
        tags=pub.GetPostData(request,'tags')
        summary=pub.GetPostData(request,'summary')
        content = pub.GetPostData(request,'content')
        status = pub.GetPostData(request,'status')
        
        ishome=pub.GetPostData(request,'ishome')
        isrecommend = pub.GetPostData(request,'isrecommend')
        istop = pub.GetPostData(request,'istop')
        isoriginal=pub.GetPostData(request,'isoriginal')
        cancomment = pub.GetPostData(request,'cancomment')
        password = pub.GetPostData(request,'password')

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

        return pub.my_render_to_response(request,"blog/pub/articleedit.html",locals())

@login_required()
def edit(request,uid,aid):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)
    channelList=Channel.objects.filter(parent_id=0)

    articleInfo=Article.objects.get(id=aid)
    oldCategory=articleInfo.category
    oldStatus=articleInfo.status

    if request.POST.has_key('ok'):
        channel1Id=int(pub.GetPostData(request,'channel1',0))
        channel2Id=int(pub.GetPostData(request,'channel2',0))
        cateId=int(pub.GetPostData(request,'category'))
        category=Category.objects.get(id=pub.GetPostData(request,'category'))

        title = pub.GetPostData(request,'title')
        pic = pub.GetPostData(request,'pic')
        tags=pub.GetPostData(request,'tags')
        summary=pub.GetPostData(request,'summary')
        content = pub.GetPostData(request,'content')
        status = pub.GetPostData(request,'status')

        ishome=pub.GetPostData(request,'ishome')
        isrecommend = pub.GetPostData(request,'isrecommend')
        istop = pub.GetPostData(request,'istop')
        isoriginal=pub.GetPostData(request,'isoriginal')
        cancomment = pub.GetPostData(request,'cancomment')
        password = pub.GetPostData(request,'password')

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
        return pub.my_render_to_response(request,"blog/pub/articleedit.html",locals())

@login_required()
def delete(request,aid,uid=-1):
    uid=int(uid)
    userInfos=viewaccounts.UsersMeta(request,uid)
    currentUser=userInfos["currentuser"]

    categoryList=viewcategory.GetCategoryList(currentUser.id)

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
    
    return HttpResponseRedirect('blog//pub/article/list/')


