#-*- coding:utf-8 -*-
import json

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

from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.common import pub,utility

from UUBlog.models import *
from UUBlog.uu.ubaseblog import *

from UUBlog.uu.ubaseadmin import UBaseAdminView


class IndexView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        tid=int(kwargs.get("tid",-1))
        order=kwargs.get("order","suggestes")

        typeList=Type.objects.filter(parent_id=0)

        if tid>0:
            blogList=Blog.objects.filter(types__contains=("%s," %tid))
            currentType=Type.objects.get(id=tid)
        else:
            blogList=Blog.objects.all()
            currentType=None

        blogList=blogList.order_by("-%s" %order)
        blogListTodayViews=Blog.objects.order_by("-todayviews")[0:30]

        followBlogIds=self.GetFollowBlogIds(uid)

        self.template_name="blog/blog.html"

        return locals()

class BaseView(UBaseAdminView):
    def GetContext(self, **kwargs):

        self.template_name="admin/setting/base.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.UpdateOption("title",self.GetPostData("title"))
            self.UpdateOption("description",self.GetPostData("description"))
            self.UpdateOption("about",self.GetPostData("about"))

            
            self.UpdateOption("dateformat",self.GetPostData("dateformat"))
            self.UpdateOption("timeformat",self.GetPostData("timeformat"))

            self.UpdateOption("email",self.GetPostData("email"))
           


            self.UpdateOption("icp",self.GetPostData("icp"))

            self.UpdateOption("close_site",self.GetPostData("close_site",False))
            self.UpdateOption("close_info",self.GetPostData("close_info"))

         


        return locals()

class AvatarView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="admin/setting/avatar.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        #000/00/01
        if self.HasPostData("ok") and self.request.FILES['avatar']:
            avatarPath=("%d" %self.currentBlog.id).rjust(7,"0")
            dir1=avatarPath[0:3]
            dir2=avatarPath[3:5]
            fileName=avatarPath[5:7]
            path="%s/%s/%s/" %("blog/avatar",dir1,dir2)

            self.currentBlog.avatar=pub.SaveFile(self.request.FILES['avatar'],path,fileName)[0]
      
            self.currentBlog.save()


        return locals()

class TemplateView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        skins=["default","temp1"]
        self.template_name="admin/template.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentBlog.template=self.GetPostData("template")
           
            self.currentBlog.save()

        return locals()

class ContentView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="admin/setting/content.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.UpdateOption("pagesize_index",self.GetPostData("pagesize_index"))
            self.UpdateOption("pagesize_user",self.GetPostData("pagesize_user"))
            self.UpdateOption("pagesize_admin",self.GetPostData("pagesize_admin"))
        return locals()

class CommentView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="admin/setting/comment.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.UpdateOption("comment_open",self.GetPostData("comment_open",False))
            self.UpdateOption("comment_interval",self.GetPostData("comment_interval",30))
            self.UpdateOption("comment_check",self.GetPostData("comment_check",False))
            self.UpdateOption("comment_code",self.GetPostData("comment_code",False))
            self.UpdateOption("comment_paging",self.GetPostData("comment_paging",False))
            self.UpdateOption("comment_pagesize",self.GetPostData("comment_pagesize",10))
            self.UpdateOption("comment_order",self.GetPostData("comment_order",True))
           


        return locals()






class OtherView(UBaseAdminView):
    def GetContext(self, **kwargs):

        self.template_name="admin/setting/other.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
           
          
            self.UpdateOption("site_title",self.GetPostData("site_title"))
            self.UpdateOption("site_keywords",self.GetPostData("site_keywords"))
            self.UpdateOption("site_description",self.GetPostData("site_description"))

            self.UpdateOption("head_html",self.GetPostData("head_html"))
            self.UpdateOption("footer_html",self.GetPostData("footer_html"))



        return locals()































