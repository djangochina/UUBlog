#-*- coding:utf-8 -*-
import os
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

from UUBlog import settings
from UUBlog.apps.blog.models import *


from django.views.generic.base import TemplateView

def my_render_to_response(request,templateName,locals):
    return render_to_response(templateName,locals,context_instance=RequestContext(request))

def HasPostData(request,key):
    if request:
        return request.POST.has_key(key)
    return False

def GetPostData(request,key,default=""):
    if HasPostData(request,key):
        return request.POST[key]
    return default

def HasGetData(request,key):
    if request:
        return request.GET.has_key(key)
    return False

def GetGetData(request,key,default=""):
    if HasGetData(request,key):
        return request.GET[key]
    return default

def GetRequestListData(request,key,default=""):
    if request:
        return request.REQUEST.getlist(key)
    return default

def GetFileInfo(filename):
    ret=[]
    ret.append(filename)
    dot=filename.rfind(".")
    if dot>-1:
        ret.append(filename[0:dot])
        ret.append(filename[dot:])
    else:
        ret.append(None)
        ret.append(None)

    return ret

#path："aaa/bbb/ccc/
#fileName:"xxx"（不带扩展名）
def SaveFile(file,path,fileName):

    fileInfo=GetFileInfo(file._get_name())


    filePath='%s%s' %(settings.MEDIA_ROOT,path)
    filePath=filePath.replace("/","\\")
    if not os.path.isdir(filePath):
        os.makedirs(filePath)
    
    fd=open(filePath+fileName+fileInfo[2],'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()

    ret=[]
    ret.append(path+fileName+fileInfo[2]) #路径+名字+文件格式
    ret.append(fileName)        #新文件名字
    ret.append(fileInfo[1])     #旧文件名字
    ret.append(fileInfo[2])     #文件格式
    return ret


def ExecuteSql(sql,isQuery=True):
    if sql is None or sql=="":
        return 

    from django.db import connection, transaction
    cursor = connection.cursor()

    cursor.execute(sql)
    if isQuery:
        fetchall = cursor.fetchall()
        return fetchall
    else:
        connection.commit()
    cursor.close() 