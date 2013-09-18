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
from UUBlog.models import *
from UUBlog.uu.ubaseblog import *

from UUBlog.uu.ubaseadmin import UBaseAdminView

categoryroot="/%d/pub/category/"

class ManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        categoryList=self.GetCatList()

        self.template_name="admin/tag.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData('ok'):
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category()
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.save()

        return locals()

class EditView(UBaseAdminView):
    

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
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()
        
        self.returnUrl=categoryroot %self.currentUser.id
        return locals()

class DeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()

        self.returnUrl=categoryroot %self.currentUser.id

        self.template_name="blog/pub/category.html"

        return locals()


    