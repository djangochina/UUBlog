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

from UUBlog.models import Category, Article,Blog,UserProfile

from django.views.generic.base import TemplateView


def categoryList(uid=-1):
    if uid>0:
        categoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)
    else:
        categoryList=Category.objects.order_by("-sortnum").all()

    return categoryList

def createUserProfile(user):
    profile=UserProfile(user=user)

    profile.nickname=user.username
    profile.save()

def createBlog(user):
  
    blog=Blog()
    blog.user_id=user.id
    blog.title=user.username+"的博客".decode("utf-8")
    blog.modules="profile,hotarticlelist,hotcommentlist"
    blog.template="default"
    blog.createtime=datetime.datetime.now()
    blog.save()

def Users(request,uid):
    uid=int(uid)
    ret={}
    
    currentUser=request.user
    if  currentUser.id :
        try:
            currentUserProfile=currentUser.get_profile()
        except:
            createUserProfile(currentUser)
            currentUserProfile=currentUser.get_profile()

        try:
            currentBlog=Blog.objects.get(user_id=currentUser.id)
        except:
            createBlog(currentUser)
            currentBlog=Blog.objects.get(user_id=currentUser.id)
    else:
        currentUser=None
        currentUserProfile=None
        currentBlog=None

    if currentUser and currentUser.id==uid:
        isMe=True
    else:
        isMe=False

    ret.setdefault("isme",isMe)
    ret.setdefault("currentuser",currentUser)
    ret.setdefault("currentuserprofile",currentUserProfile)
    ret.setdefault("currentblog",currentBlog)


    if uid>0:
        try:
            isGuest=True
            guestUser=User.objects.get(id=uid)
        except:
            isGuest=False
            guestUser=None
            guestUserProfile=None
            guestBlog=None
    
        if isGuest:
            try:
                try:
                    guestUserProfile=guestUser.get_profile()
                except:
                    createUserProfile(guestUser)
                    guestUserProfile=guestUser.get_profile()

                try:
                    guestBlog=Blog.objects.get(user_id=guestUser.id)
                except:
                    createBlog(guestUser)
                    guestBlog=Blog.objects.get(user_id=guestUser.id)
            except:
                guestUserProfile=False
                guestBlog=None
    else:
        isGuest=False
        guestUser=None
        guestUserProfile=None
        guestBlog=None

    ret.setdefault("isguest",isGuest)
    ret.setdefault("guestuser",guestUser)
    ret.setdefault("guestuserprofile",guestUserProfile)
    ret.setdefault("guestblog",guestBlog)

    return ret
