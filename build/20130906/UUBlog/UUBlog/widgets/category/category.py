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
from UUBlog.uu.ubasewidget import *

config={}
config.setdefault("name","category")
config.setdefault("title","分类")
config.setdefault("description","分类")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class CategorySetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(CategorySetting, self).__init__(**kwargs)
        self.InitValue(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("width",self.GetPostData('width'))
        params.setdefault("height",self.GetPostData('height'))

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')


def CategoryView(uBaseBlog,widget,kwargs={}):
    catTreeHtml=uBaseBlog.BuildCatTreeHtml(0,-1)

    categoryList=Category.objects.order_by("-sortnum").all()

    return catTreeHtml



config.setdefault("setting",CategorySetting)
config.setdefault("view",CategoryView)




