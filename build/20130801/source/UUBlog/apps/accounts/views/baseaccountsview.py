#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView

from UUBlog.apps.blog.models import *
from UUBlog.apps.blog import modules

class UBaseAccountsView(UBaseTemplateView):

    
    def __init__(self, **kwargs):
        super(UBaseAccountsView, self).__init__(**kwargs)

        self.userInfos=None
        self.currentUser=None
        self.currentUserProfile=None
        self.currentBlog=None
        self.guestUser=None
        self.guestUserProfile=None
        self.guestBlog=None
        self.randBlog=None

        self.fields={}

    def ResetUserInfos(self,uid):
        from UUBlog.apps.accounts.views import viewaccounts
        self.userInfos=viewaccounts.UsersMeta(self.request,uid)
        self.currentUser=self.userInfos["currentuser"]
        self.currentUserProfile=self.userInfos["currentuserprofile"]
        self.currentBlog=self.userInfos["currentblog"]

        self.guestUser=self.userInfos["guestuser"]
        self.guestUserProfile=self.userInfos["guestuserprofile"]
        self.guestBlog=self.userInfos["guestblog"]
        self.randBlog=Blog.objects.order_by("?")[0]

        self.fields={
            "userInfos":self.userInfos,
            "currentUser":self.currentUser,
            "currentUserProfile":self.currentUserProfile,
            "currentBlog":self.currentBlog,
            "guestUser":self.guestUser,
            "guestUserProfile":self.guestUserProfile,
            "guestBlog":self.guestBlog,
            "randBlog":self.randBlog,
        }

    def post_context_data(self, **kwargs):
        context= super(UBaseAccountsView, self).post_context_data(**kwargs)
        uid=int(kwargs.get("uid",0))
        
        self.ResetUserInfos(uid)

        myContext=self.PostContext(**kwargs)
        
        self.AddVars(context,myContext)

        self.AddVars(context,self.fields)

        self.AddVars(context,locals())

        return context


    def get_context_data(self, **kwargs):
        context= super(UBaseAccountsView, self).get_context_data(**kwargs)

        uid=int(kwargs.get("uid",0))
        
        self.ResetUserInfos(uid)

        myContext=self.GetContext(**kwargs)
        self.AddVars(context,myContext)

        self.AddVars(context,self.fields)

        self.AddVars(context,locals())

        return context

    def PostContext(self,**kwargs):
        context={}
        return context
    def GetContext(self,**kwargs):
        context={}
        return context



  




























