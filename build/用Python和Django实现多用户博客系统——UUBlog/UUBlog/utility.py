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
import os
import re
import settings

from django.views.generic.base import TemplateView


def my_render_to_response(request,templateName,locals):
    return render_to_response(templateName,locals,context_instance=RequestContext(request))

def HasPostData(request,key):
    return request.POST.has_key(key)

def GetPostData(request,key,default=""):
    if request.POST.has_key(key):
        return request.POST[key]
    return default



def RemoveTags(str_html):
    return re.compile('</?\w+[^>]*>').sub('',str_html)


def SaveFile(file,path='',fileName=''):
    tempFileName=file._get_name()
    dot=tempFileName.index(".")

    fileName=tempFileName[0:dot] if fileName=='' else fileName
    fileName=fileName+tempFileName[dot:]

    filePath='%s%s' %(settings.MEDIA_ROOT,path)
    filePath=filePath.replace("/","\\")
    if not os.path.isdir(filePath):
        os.makedirs(filePath)

    fd=open(filePath+fileName,'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    return (path+fileName)
















