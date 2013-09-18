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
    if kwargs.has_key("request") and kwargs.has_key("uid"):
        request=kwargs["request"]
        uid=kwargs["uid"]
        

        from UUBlog.apps.accounts.views import viewaccounts
        return viewaccounts.UsersMeta(request,uid)
    else:
        return None

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

#Ta关注的
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

#关注Ta的（粉丝）
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


def GetWidgetData(func,kwargs={}):
    ret={}
    try:
        ret = eval(func)(kwargs)
    except:
        ret={}
    
    return ret