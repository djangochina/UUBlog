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

#用户博客首页
class HomeView(UBaseBlogView):

    def GetContext(self, **kwargs):
        from django.views.generic import RedirectView

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
class ShowView(UBaseBlogView):

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
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

            self.guestBlog.comments+=1
            self.guestBlog.save()

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

        if self.HasPostData("ok"):
            username = self.GetPostData('username')
            content = self.GetPostData('content')

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

        #更新文章浏览量
        articleInfo.views+=1
        articleInfo.save()

        commentList=Comment.objects.filter(article_id=aid)


        self.template_name="blog/skins/"+self.guestBlog.template+"/show.html"

        return locals()

#分类浏览
class CategoryView(UBaseBlogView):


    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        moduleList=self.GetBlogModuleList(uid)
        navigateCategoryList=self.GetNavigateCategoryList(uid)
        followBlogIds=self.GetFollowBlogIds(uid)
        suggestBlogIds=self.GetSuggestBlogIds(uid)

        articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

        #更新用户文章总数
        self.guestBlog.todayviews+=1
        self.guestBlog.totalviews+=1
        self.guestBlog.save()
    
        self.AddVisit(uid)

        self.template_name="blog/skins/"+self.guestBlog.template+"/home.html"

        return locals()

#Tag浏览
class TagView(UBaseBlogView):


    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        moduleList=self.GetBlogModuleList(uid)
        navigateCategoryList=self.GetNavigateCategoryList(uid)
        followBlogIds=self.GetFollowBlogIds(uid)
        suggestBlogIds=self.GetSuggestBlogIds(uid)

        articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(category_id=cid).filter(status=1)

        #更新用户文章总数
        self.guestBlog.todayviews+=1
        self.guestBlog.totalviews+=1
        self.guestBlog.save()
    
        self.AddVisit(uid)

        self.template_name="blog/skins/"+self.guestBlog.template+"/home.html"

        return locals()

#文章管理列表
class PubListView(UBaseBlogView):

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        draft=kwargs.get("draft",None)
        cid=int(kwargs.get("cid",-1))

        categoryList=self.GetCategoryList(self.currentUserProfile.user_id)

        articleList=Article.objects.order_by("-createtime").filter(user_id=self.currentUserProfile.user_id)

        if draft:
            articleList=articleList.filter(status=0)

        if cid and cid>0:
            articleList=articleList.filter(category_id=cid)

        self.template_name="blog/pub/articlelist.html"

        return locals()

#文章添加
class ArticleAddView(UBaseBlogView):

    def GetContext(self, **kwargs):

        categoryList=self.GetCategoryList(self.currentBlog.id)
        channelList=Channel.objects.filter(parent_id=0)

        articleInfo=Article()

        self.template_name="blog/pub/articleedit.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            channel1Id=int(self.GetPostData('channel1',0))
            channel2Id=int(self.GetPostData('channel1',0))

            category=Category.objects.get(id=self.GetPostData('category'))

            articleInfo=Article()
            articleInfo.category=category
            articleInfo.createtime=datetime.datetime.now()
            articleInfo.user_id=self.currentUser.id
            articleInfo.username=self.currentUser.username
            SetArticleValues(self.request,articleInfo)

            articleInfo.save()

            #更新分类统计信息 不是默认分类并且是发布的文章
            if category.id !=1 and articleInfo.status:
                category.articles+=1
                category.save()

            #更新用户文章统计信息
            self.currentBlog.articles+=1
            self.currentBlog.save()

            self.UpdateChannelArticles(channel1Id,channel2Id)
        

        self.template_name="blog/pub/articleedit.html"

        return locals()

#文章修改
class ArticleEditView(UBaseBlogView):

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        aid=int(kwargs.get("aid",0))

        categoryList=self.GetCategoryList(self.currentBlog.id)
        channelList=Channel.objects.filter(parent_id=0)

        articleInfo=Article.objects.get(id=aid)

        self.template_name="blog/pub/articleedit.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        aid=int(kwargs.get("aid",0))

        articleInfo=Article.objects.get(id=aid)

        oldCategory=articleInfo.category
        oldStatus=articleInfo.status

        if self.HasPostData('ok'):
        
            category=Category.objects.get(id=self.GetPostData('category'))

            articleInfo.category=category
            SetArticleValues(self.request,articleInfo)

            if oldCategory != category:
                #不是未分类，并且已经发布
                if category.id !=1 and articleInfo.status:
                    category.articles+=1
                    category.save()
                #不是未分类，并且已经是草稿
                if oldCategory.id!=1 and oldStatus:
                    oldCategory.articles=oldCategory.articles-1 if oldCategory.articles>1 else 0
                    oldCategory.save()
            else:
                if not articleInfo.status:
                    category.articles-=1
                    category.save()

        
            articleInfo.save()


        self.template_name="blog/pub/articleedit.html"

        return locals()


def SetArticleValues(request,articleInfo):
    channel1Id=int(pub.GetPostData(request,'channel1',0))
    channel2Id=int(pub.GetPostData(request,'channel1',0))

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
   

    articleInfo.ishome=1 if ishome else 0
    articleInfo.isrecommend=1 if isrecommend else 0
    articleInfo.istop=1 if istop else 0
    articleInfo.isoriginal=1 if isoriginal else 0
    articleInfo.cancomment=1 if cancomment else 0
    articleInfo.password=password

#文章删除
class ArticleDeleteView(UBaseBlogView):

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        aid=int(kwargs.get("aid",0))
        

        categoryList=self.GetCategoryList(uid)

        articleInfo=Article.objects.get(id=aid)
    
        if articleInfo.status:
            category=articleInfo.category

            #更新分类统计信息
            if category.articles>0:
                category.articles-=1
                category.save()

            if self.currentBlog.articles>0:
                self.currentBlog.articles-=1
                self.currentBlog.save()

        articleInfo.delete()

        articleList=Article.objects.order_by("-createtime").filter(user_id=currentUser.id)
    

        return HttpResponseRedirect('blog/pub/article/list/')

        return locals()


