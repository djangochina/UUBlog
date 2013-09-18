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
from UUBlog.common import pub,utility
from django.utils import simplejson as json
from django.contrib.auth.models import User


def checkdata(request):

    isExist=False
    ele=pub.GetGetData(request,"ele")
    data=pub.GetGetData(request,"data")
    if ele=="username" :
        user=User.objects.filter(username=data)
        
    else:
        user=User.objects.filter(email=data)

    if user:
            isExist=True

    retjson=json.dumps({"isExist":isExist})
    return HttpResponse(retjson)

