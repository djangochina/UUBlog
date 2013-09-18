#-*- coding:utf-8 -*-
import uuid
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

#用户博客首页
class IndexView(UBaseAdminView):

    def GetContext(self, **kwargs):

        myWidgetList=self.GetWidgetList()
       
        postList=self.GetPostList()
      
      

        self.template_name="admin/index.html"

        return locals()



  



    
    
    
    
    
    
    
    
    
               