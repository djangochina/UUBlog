#-*- coding:utf-8 -*-

import time,datetime

from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

from django.views.generic.base import TemplateView
from django.views import generic
from django.db.models import Q
from django.db import connection
from django.template import RequestContext 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from UUBlog.common import pub,utility
from UUBlog.apps.accounts.models import *
from UUBlog.apps.blog.models import *
from UUBlog.apps.blog import modules


def register(request):
    if pub.HasPostData(request,"ok"):
        username=pub.GetPostData(request,"username")
        password=pub.GetPostData(request,"password")
        email=pub.GetPostData(request,"email")

        user=User.objects.create_user(username,email,password)
        user.first_name=username
        user.save()

        createUserProfile(user)

        from UUBlog.apps.blog.views import viewblog
        viewblog.createBlog(user)

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/register.html",locals())

def login(request):
    if pub.HasPostData(request,"ok"):
        username=pub.GetPostData(request,"username")
        password=pub.GetPostData(request,"password")

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            userProfile=user.get_profile()
            try:
                userProfile=user.get_profile()
            except:
                createUserProfile(user)
            try:
                blog=Blog.objects.get(id=user.id)
            except:
                from UUBlog.apps.blog.views import viewblog
                viewblog.createBlog(user)

            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('')
    else:
        return pub.my_render_to_response(request,"accounts/login.html",locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')



def createUserProfile(user):
    profile=UserProfile(user=user)

    profile.nickname=user.username
    profile.save()



#头像
@login_required()
def avatar(request,uid=-1):
    userInfos=UsersMeta(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]
    #000/00/01
    if pub.HasPostData(request,"ok"):
        avatarPath=("%d" %currentUserProfile.user_id).rjust(7,"0")
        dir1=avatarPath[0:3]
        dir2=avatarPath[3:5]
        fileName=avatarPath[5:7]
        path="%s/%s/%s/" %("avatar",dir1,dir2)

        currentUserProfile.avatar=pub.SaveFile(request.FILES['avatar'],path,fileName)
      
        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/pub/avatar.html",locals())


#基本信息
@login_required()
def base(request,uid=-1):
    userInfos=UsersMeta(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if pub.HasPostData(request,"ok"):
        currentUserProfile.nickname=pub.GetPostData(request,"nickname")
        currentUserProfile.realname=pub.GetPostData(request,"realname")
        currentUserProfile.gender=pub.GetPostData(request,"gender")
        currentUserProfile.birthday=pub.GetPostData(request,"birthday")
        currentUserProfile.birthcity=pub.GetPostData(request,"birthcity")
        currentUserProfile.residecity=pub.GetPostData(request,"residecity")
      
        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/pub/base.html",locals())


#个人信息
@login_required()
def info(request,uid=-1):
    userInfos=UsersMeta(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if pub.HasPostData(request,"ok"):
        currentUserProfile.affectivestatus=pub.GetPostData(request,"affectivestatus")
        currentUserProfile.lookingfor=pub.GetPostData(request,"lookingfor")
        currentUserProfile.bloodtype=pub.GetPostData(request,"bloodtype")
        currentUserProfile.site=pub.GetPostData(request,"site")
        currentUserProfile.bio=pub.GetPostData(request,"bio")
        currentUserProfile.interest=pub.GetPostData(request,"interest")
        currentUserProfile.sightml=pub.GetPostData(request,"sightml")
        currentUserProfile.timeoffset=pub.GetPostData(request,"timeoffset")

        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/pub/info.html",locals())


#联系方式
@login_required()
def contact(request,uid=-1):
    userInfos=UsersMeta(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if pub.HasPostData(request,"ok"):
        currentUserProfile.qq=pub.GetPostData(request,"qq")
        currentUserProfile.msn=pub.GetPostData(request,"msn")
        currentUserProfile.taobao=pub.GetPostData(request,"taobao")
        currentUserProfile.email=pub.GetPostData(request,"email")
        currentUserProfile.phone=pub.GetPostData(request,"phone")
        currentUserProfile.mobile=pub.GetPostData(request,"mobile")
        currentUserProfile.address=pub.GetPostData(request,"address")
        currentUserProfile.zipcode=pub.GetPostData(request,"zipcode")

        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/pub/contact.html",locals())


#安全
@login_required()
def security(request,uid=-1):
    userInfos=UsersMeta(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if pub.HasPostData(request,"ok"):
        currentUserProfile.avatar=utility.SaveFile(request.FILES['avatar'],'avatar/')
      
        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return pub.my_render_to_response(request,"accounts/pub/security.html",locals())













def UsersMeta(request,uid):
    currentUser=request.user
    uid=int(uid)
    ret={}

    #user begin
    if not currentUser or not currentUser.id:
        currentUser=None
         
    if currentUser and currentUser.id==uid:
        isMe=True
    else:
        isMe=False
    ret.setdefault("isme",isMe)
    ret.setdefault("currentuser",currentUser)

    if uid>0:
        try:
            isGuest=True
            guestUser=User.objects.get(id=uid)
        except:
            isGuest=False
            guestUser=None
    else:
        isGuest=False
        guestUser=None

    ret.setdefault("isguest",isGuest)
    ret.setdefault("guestuser",guestUser)
    # user end

    #userprofile begin
    currentUserProfile=None
    if  currentUser:
        try:
            currentUserProfile=currentUser.get_profile()
        except:
            #createUserProfile(currentUser)
            #currentUserProfile=currentUser.get_profile()
            currentUserProfile=None
    ret.setdefault("currentuserprofile",currentUserProfile)

    guestUserProfile=None
    if guestUser:
        try:
            guestUserProfile=guestUser.get_profile()
        except:
            #createUserProfile(guestUser)
            #guestUserProfile=guestUser.get_profile()
            guestUserProfile=None
    ret.setdefault("guestuserprofile",guestUserProfile)
    #userprofile end

    #blog begin
    currentBlog=None
    if currentUser:
        try:
            currentBlog=Blog.objects.get(id=currentUser.id)
        except:
            #createBlog(currentUser)
            #currentBlog=Blog.objects.get(id=currentUser.id)
            currentBlog=None
    ret.setdefault("currentblog",currentBlog)

    guestBlog=None
    if guestUser:
        try:
            guestBlog=Blog.objects.get(id=guestUser.id)
        except:
            #createBlog(guestUser)
            #guestBlog=Blog.objects.get(id=guestUser.id)
            guestBlog=None
    ret.setdefault("guestblog",guestBlog)
    #blog end



    return ret