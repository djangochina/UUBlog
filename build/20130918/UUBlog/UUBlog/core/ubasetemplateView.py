#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from django.views.generic.base import TemplateView

from UUBlog.common import pub


class UBaseTemplateView(TemplateView):
    extraContext={}
    
    def __init__(self, **kwargs):
        super(UBaseTemplateView, self).__init__(**kwargs)
        self.template_name=""
        self.redirectUrl=None
        self.autoRedirect=True
        self.currentUrl="/"
        self.currentQueryString=None
        self.currentFullUrl="/"
        self.currentQueryDic={}
        self.message=None


    def post(self, request, *args, **kwargs):
        self.redirectUrl=request.path
        
        self.post_context_data(**kwargs)
        #context = self.post_context_data(**kwargs)       
        
        if self.redirectUrl is None:
            self.redirectUrl="/"
        return HttpResponseRedirect(self.redirectUrl)

    def post_context_data(self, **kwargs):
        context={}

        self.AddVars(context,**kwargs)

        return context

    def get(self, request, *args, **kwargs):
        self.redirectUrl=None

        self.currentUrl=self.request.META["PATH_INFO"]
        self.currentQueryString=self.request.META["QUERY_STRING"]
        
        if self.currentQueryString is None or self.currentQueryString=="":
            self.currentFullUrl=self.currentUrl
        else:
            self.currentFullUrl="%s?%s" %(self.currentUrl,self.currentQueryString)
        self.currentQueryDic=self.request.GET.copy()

        context = self.get_context_data(**kwargs)

        if self.autoRedirect and self.redirectUrl is not None:
            if self.currentQueryString is None  or self.currentQueryString=="":
                pass
            else:
                self.redirectUrl=self.redirectUrl+"?"+self.currentQueryString

            return HttpResponseRedirect(self.redirectUrl)
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
    def SetTemplateName(self,templateName):
        self.template_name=templateName
                    
    def CheckTemplateExists(self,templateName=""):
        if templateName is None or templateName=="":
            templateName=self.template_name
       
        try:
            from django import template
            template.loader.get_template(templateName)
            return True
        except:
            return False

    #cookie、session
    def SetCookie(self,response,key,value):
        response.set_cookie(key,value)
    
    def GetCookie(self,key,defaultValue=None):
        return pub.GetCookie(self.request,key,defaultValue)
        
    def DelCookie(self,response,key):
        response.delete_cookie(key,path="/")
   
    def HasSession(self,key):
        return pub.HasSession(self.request,key)

    def SetSession(self,key,value):
        pub.SetSession(self.request,key,value)

    def GetSession(self,key,defaultValue=None,isDelete=False):
        return pub.GetSession(self.request,key,defaultValue,isDelete)

    def DelSession(self,key):
        pub.DelSession(self.request,key)
    
    #post、get、file
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














