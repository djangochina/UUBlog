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
from UUBlog.uu.ubaseadmin import UBaseAdminView


class CatManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)

        catList=self.GetCategoryList()

        self.template_name="admin/catlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            sortnum=self.GetPostData("sortnum",0)

            catInfo=Category()
            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0

            catInfo.save()

        return locals()

class CatEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        cid=int(kwargs.get("cid",0))

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,cid)

        

        catInfo=Category.objects.get(id=cid)

        self.template_name="admin/cat.html"

        return locals()

    def PostContext(self, **kwargs):
       
        if self.HasPostData('ok'):
            cid=int(kwargs.get("cid",0))
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            sortnum=self.GetPostData("sortnum",0)

            catInfo=Category.objects.get(id=cid)
            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0

            catInfo.save()
        
        self.returnUrl="/admin/catlist"
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


    