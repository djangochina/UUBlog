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
from UUBlog.models import Category, Article,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import common

import utility

#头像
@login_required()
def avatar(request,uid=-1):
    userInfos=common.Users(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]
    #000/00/01
    if utility.HasPostData(request,"ok"):
        avatarPath=("%d" %currentUserProfile.user_id).rjust(7,"0")
        dir1=avatarPath[0:3]
        dir2=avatarPath[3:5]
        fileName=avatarPath[5:7]
        path="%s/%s/%s/" %("avatar",dir1,dir2)

        currentUserProfile.avatar=utility.SaveFile(request.FILES['avatar'],path,fileName)
      
        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/profile/avatar.html",locals())


#基本信息
@login_required()
def base(request,uid=-1):
    userInfos=common.Users(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if utility.HasPostData(request,"ok"):
        currentUserProfile.nickname=utility.GetPostData(request,"nickname")
        currentUserProfile.realname=utility.GetPostData(request,"realname")
        currentUserProfile.gender=utility.GetPostData(request,"gender")
        currentUserProfile.birthday=utility.GetPostData(request,"birthday")
        currentUserProfile.birthcity=utility.GetPostData(request,"birthcity")
        currentUserProfile.residecity=utility.GetPostData(request,"residecity")
      
        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/profile/base.html",locals())


#个人信息
@login_required()
def info(request,uid=-1):
    userInfos=common.Users(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if utility.HasPostData(request,"ok"):
        currentUserProfile.affectivestatus=utility.GetPostData(request,"affectivestatus")
        currentUserProfile.lookingfor=utility.GetPostData(request,"lookingfor")
        currentUserProfile.bloodtype=utility.GetPostData(request,"bloodtype")
        currentUserProfile.site=utility.GetPostData(request,"site")
        currentUserProfile.bio=utility.GetPostData(request,"bio")
        currentUserProfile.interest=utility.GetPostData(request,"interest")
        currentUserProfile.sightml=utility.GetPostData(request,"sightml")
        currentUserProfile.timeoffset=utility.GetPostData(request,"timeoffset")

        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/profile/info.html",locals())


#联系方式
@login_required()
def contact(request,uid=-1):
    userInfos=common.Users(request,-1)
    currentUserProfile=userInfos["currentuserprofile"]

    if utility.HasPostData(request,"ok"):
        currentUserProfile.qq=utility.GetPostData(request,"qq")
        currentUserProfile.msn=utility.GetPostData(request,"msn")
        currentUserProfile.taobao=utility.GetPostData(request,"taobao")
        currentUserProfile.email=utility.GetPostData(request,"email")
        currentUserProfile.phone=utility.GetPostData(request,"phone")
        currentUserProfile.mobile=utility.GetPostData(request,"mobile")
        currentUserProfile.address=utility.GetPostData(request,"address")
        currentUserProfile.zipcode=utility.GetPostData(request,"zipcode")

        currentUserProfile.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/profile/contact.html",locals())


#安全
@login_required()
def security(request,uid=-1):
    userInfos=common.Users(request,-1)
    userProfile=userInfos[2]

    if utility.HasPostData(request,"ok"):
        userProfile.avatar=utility.SaveFile(request.FILES['avatar'],'avatar/')
      
        userProfile.save()

        return HttpResponseRedirect('/')
    else:
        return utility.my_render_to_response(request,"pub/profile/security.html",locals())
















