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
from UUBlog.apps.blog import modules
from UUBlog.apps.blog.views.baseblogview import *

categoryroot="/%d/pub/category/"

class IndexView(UBaseBlogView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        categoryList=self.GetCategoryList(uid)

        self.template_name="blog/pub/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData('ok'):
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")

            categoryInfo=Category()
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.user_id=self.currentUser.id
            categoryInfo.save()

        return locals()

class CategoryEditView(UBaseBlogView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        categoryInfo=Category.objects.get(id=cid)

        self.template_name="blog/pub/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.save()
        
        self.returnUrl=categoryroot %self.currentUser.id
        return locals()

class CategoryDeleteView(UBaseBlogView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()


    