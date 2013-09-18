#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

from django.db import models

from UUBlog.common import pub, utility


class UBaseTemplateView(TemplateView):
    extraContext={}
    returnUrl=None
    currentUrl="/"
    currentQueryString=None
    currentFullUrl="/"
    currentQueryDic={}
    def __init__(self, **kwargs):
        super(UBaseTemplateView, self).__init__(**kwargs)
        self.template_name=""

    def post(self, request, *args, **kwargs):
        self.returnUrl=request.path

        context = self.post_context_data(**kwargs)
        
        if self.returnUrl is None:
            self.returnUrl="/"
        return HttpResponseRedirect(self.returnUrl)

    def post_context_data(self, **kwargs):
        context={}

        self.AddVars(context,**kwargs)

        return context

    def get(self, request, *args, **kwargs):
        self.returnUrl=None

        self.currentUrl=self.request.META["PATH_INFO"]
        self.currentQueryString=self.request.META["QUERY_STRING"]
        
        if self.currentQueryString is None or self.currentQueryString=="":
            self.currentFullUrl=self.currentUrl
        else:
            self.currentFullUrl="%s?%s" %(self.currentUrl,self.currentQueryString)
        self.currentQueryDic=self.request.GET.copy()

        context = self.get_context_data(**kwargs)

        if self.returnUrl is not None:
            if self.currentQueryString is None  or self.currentQueryString=="":
                pass
            else:
                self.returnUrl=self.returnUrl+"?"+self.currentQueryString

            return HttpResponseRedirect(self.returnUrl)
        else:
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(UBaseTemplateView, self).get_context_data(**kwargs)

        self.AddVars(context,**kwargs)
        self.AddVars(context,self.extraContext)
       
        return context

    def PostContext(self,**kwargs):
        context={}
        return context
    def GetContext(self,**kwargs):
        context={}
        return context

    def BuildQueryString(self,queryDic=None,**appendQueryString):
        
        if queryDic==None:
            queryDic=self.currentQueryDic

        for key,value in appendQueryString.items():
            if queryDic.has_key(key):
                if value is None:
                    del queryDic[key]
                else:
                    queryDic[key]=value
            else:
                queryDic.setdefault(key,value)

        retQueryString=""
        for key,value in queryDic.items():
            retQueryString+="%s=%s&" %(key,value)
        
        return retQueryString.rstrip("&")

    def AddVars(self,context,args={},**kwargs):
        if args:
            for key, value in args.items():
                context[key]=value

        if kwargs:
            for key, value in kwargs.items():
                context[key]=value
            

    def HasPostData(self,key):
        return pub.HasPostData(self.request,key)

    def GetPostData(self,key,default=""):
        return pub.GetPostData(self.request,key,default)

    def HasGetData(self,key):
        return pub.HasGetData(self.request,key)

    def GetGetData(self,key,default=""):
        return pub.GetGetData(self.request,key,default)

    def GetRequestListData(self,key,default=""):
        return pub.GetRequestListData(self.request,key,default)
        
    def HasFile(self,key):
        return pub.HasFile(self.request,key)

    def GetFile(self,key):
        return pub.GetFile(self.request,key)














