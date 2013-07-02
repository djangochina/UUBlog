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


from UUBlog.apps.blog.models import *
from UUBlog.apps.accounts.models import UserProfile



def ProfileModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        userProfile=UserProfile.objects.get(user_id=uid)
    else:
        userProfile=None
    
    return userProfile

def ArchiveModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    if uid>-1:
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]
    return articleList

def CategoryModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        categoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)
    else:
        categoryList=Category.objects.order_by("-sortnum").all()

    return categoryList

def SearchModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]
 
    return articleList

def TagsModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    if uid>-1:
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]
    return articleList

def HotArticleListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]
    return articleList

def NewArticleListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-createtime").filter(status=1)[:5]

    return articleList

def GoodArticleListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    return articleList

def BadArticleListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    return articleList

def HotCommentListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-comments").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-comments").filter(status=1)[:5]

    return articleList

def NewCommentListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    return articleList

def GoodCommentListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]

    return articleList

def BadCommentListModule(kwargs={}):
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        articleList=Article.objects.order_by("-views").filter(user_id=uid).filter(status=1)[:5]
    else:
        articleList=Article.objects.order_by("-views").filter(status=1)[:5]
    
    return articleList

def HotUserListModule(kwargs={}):
    userList=User.objects.order_by("-id").all()
    return userList

def NewUserListModule(kwargs={}):
    userList=User.objects.order_by("-id").all()
    return userList


def FollowBlogListModule(kwargs={}):
    followBlogList=[]
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        blog=Blog.objects.get(id=uid)
        followList=Follow.objects.filter(blog_id=blog.id)
        for follow in followList:
            followBlog=Blog.objects.get(id=follow.follow_blog_id)
            followBlogList.append(followBlog)


    return followBlogList

def BeFollowBlogListModule(kwargs={}):
    beFollowBlogList=[]
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        blog=Blog.objects.get(id=uid)
        beFollowList=Follow.objects.filter(follow_blog_id=blog.id)
        for beFollow in beFollowList:
            beFollowBlog=Blog.objects.get(id=beFollow.blog_id)
            beFollowBlogList.append(beFollowBlog)


    return beFollowBlogList

#访问我的
def BeVisitBlogListModule(kwargs={}):
    beVisitBlogList=[]
    if kwargs.has_key("uid"):
        uid=kwargs["uid"]
        blog=Blog.objects.get(id=uid)
        beVisitList=Visit.objects.filter(visit_blog_id=blog.id).order_by("-lastvisittime")
        for beVisit in beVisitList:
            beVisitBlog=Blog.objects.get(id=beVisit.blog_id)
            beVisitBlogList.append(beVisitBlog)


    return beVisitBlogList

moduleList={
    "profile":{"name":"个人资料","action":ProfileModule},
    "archive":{"name":"归档","action":ArchiveModule},
    "category":{"name":"分类","action":CategoryModule},
    "search":{"name":"搜索","action":SearchModule},
    "tags":{"name":"Tags","action":TagsModule},
    "hotarticlelist":{"name":"热门文章","action":HotArticleListModule},
    "newarticlelist":{"name":"最新文章","action":NewArticleListModule},
    "goodarticlelist":{"name":"推荐文章","action":GoodArticleListModule},
    "badarticlelist":{"name":"鄙视文章","action":BadArticleListModule},
    "hotcommentlist":{"name":"热门评论","action":HotCommentListModule},
    "newcommentlist":{"name":"最新评论","action":NewCommentListModule},
    "goodcommentlist":{"name":"推荐评论","action":GoodCommentListModule},
    "badcommentlist":{"name":"鄙视评论","action":BadCommentListModule},
    "hotuserlist":{"name":"热门用户","action":HotUserListModule},
    "newuserlist":{"name":"最新用户","action":NewUserListModule},
    "followbloglist":{"name":"Ta关注的","action":FollowBlogListModule},
    "befollowbloglist":{"name":"关注Ta的","action":BeFollowBlogListModule},
    "bevisitbloglist":{"name":"最近访客","action":BeVisitBlogListModule},



}

def GetModuleName(key):
    if moduleList.has_key(key):
        moduleInfo=moduleList[key]
        return moduleInfo["name"]
    return None

def GetModuleAction(key):
    if moduleList.has_key(key):
        moduleInfo=moduleList[key]
        return moduleInfo["action"]
    return None

def GetModuleList(kwargs={}):
    ret={}
    for key in kwargs.keys():
        if moduleList.has_key(key):
            moduleInfo=moduleList[key]
            value=moduleInfo["action"](kwargs[key])
            ret.setdefault(key,value)
        
    return ret