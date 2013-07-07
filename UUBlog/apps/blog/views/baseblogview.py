#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.apps.accounts.views import viewaccounts
from UUBlog.apps.blog.models import *
from UUBlog.apps.blog import modules

class UBaseBlogView(UBaseTemplateView):

    
    def __init__(self, **kwargs):
        super(UBaseBlogView, self).__init__(**kwargs)

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
        context= super(UBaseBlogView, self).post_context_data(**kwargs)
        uid=int(kwargs.get("uid",0))
        
        self.ResetUserInfos(uid)

        myContext=self.PostContext(**kwargs)
        
        self.AddVars(context,myContext)

        self.AddVars(context,self.fields)

        self.AddVars(context,locals())

        return context


    def get_context_data(self, **kwargs):
        context= super(UBaseBlogView, self).get_context_data(**kwargs)

        uid=int(kwargs.get("uid",0))
        
        self.ResetUserInfos(uid)

        myContext=self.GetContext(**kwargs)
        self.AddVars(context,myContext)

        self.AddVars(context,self.fields)

        self.AddVars(context,locals())

        return context





    def IsMyBlog(self,uid):
        if self.currentBlog and self.guestBlog and self.currentBlog.id==self.guestBlog.id:
            return True
        return False

    #我的模块列表
    def GetBlogModuleList(self,uid):
        moduleList=None
        if self.guestBlog:
            myModules=self.guestBlog.modules.split(",")
            moduleParams={}
            for myModule in myModules:
                moduleParams.setdefault(myModule,{"uid":uid})

            moduleList=modules.GetModuleList(moduleParams)

        return moduleList

    #我关注的博客id
    def GetFollowBlogIds(self,uid):
        followBlogIds=[]
        if self.currentBlog:
            followList=Follow.objects.filter(blog_id=self.currentBlog.id)
            for follow in followList:
                followBlogIds.append(follow.follow_blog_id)

        return followBlogIds

    #我推荐的博客id
    def GetSuggestBlogIds(self,uid):
        suggestBlogIds=[]
        if self.currentBlog:
            suggestList=Suggest.objects.filter(blog_id=self.currentBlog.id)
            for suggest in suggestList:
                suggestBlogIds.append(suggest.suggest_blog_id)

        return suggestBlogIds

    #文章分类
    def GetCategoryList(self,uid):
        categoryList=Category.objects.order_by("-sortnum").filter(user_id=uid)

        return categoryList

    #在博客菜单显示的分类
    def GetNavigateCategoryList(self,uid):
        navigateCategoryList=Category.objects.order_by("-sortnum").filter(user_id=uid,isnav=1)

        return navigateCategoryList

    #文章列表
    def GetArticleList(self,uid,*order,**kwargs):
        articleList=Article.objects.order_by("-createtime").filter(user_id=uid).filter(status=1)
        if kwargs:
            articleList=articleList.filter(**kwargs)
        
        return articleList


    #添加访客
    def AddVisit(self,uid):
        if self.currentUser and not self.IsMyBlog(uid):
            visit=Visit.objects.filter(blog_id=self.currentBlog.id,visit_blog_id=self.guestBlog.id)
            if not visit:
                visit=Visit()
                visit.blog_id=self.currentBlog.id
                visit.visit_blog_id=self.guestBlog.id
                visit.lastvisittime=datetime.datetime.now()
                visit.save()

    #更新频道文章数量
    def UpdateChannelArticles(self,num=1,*channelIds):
        if channelIds:
            for channelId in channelIds:
                if channelId>0:
                    try:
                        channelInfo=Channel.objects.get(id=channelId)
                        channelInfo.articles+=num
                        channelInfo.save()
                    except:
                        pass




























