#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.apps.accounts.views import viewaccounts
from UUBlog.apps.blog.models import *
from UUBlog.apps.blog import widgets

from UUBlog.common import utility,pub

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
    def GetBlogWidgetList(self,uid):
        retWidgetList=[]

        if self.guestBlog:
            #获取博客的widget
            tempWidgetList=BlogWidget.objects.filter(blog_id=self.guestBlog.id).order_by("-sortnum")
            
            
            for tempWidget in tempWidgetList:
                
                widgetInfo=tempWidget.widget

                #widget属性值，返回字典格式如：{"width":300,"height":500}
                widgetValue=utility.Json2Obj(tempWidget.attvalues,{})

                

                #widget的name
                widgetValue.setdefault("name",widgetInfo.name)

                #标题
                widgetValue.setdefault("title",tempWidget.title)
                
                #博客id
                widgetValue.setdefault("blogid",self.guestBlog.id)

                #render模板
                widgetValue.setdefault("render",widgetInfo.render)

                datas=None
                if tempWidget.widget.issys==1:

                    #通过函数调用
                    if widgetInfo.datafrom=="func":
                        params=utility.Json2Obj(tempWidget.params,{})
                        
                        params.setdefault("uid",self.guestBlog.id) 
                        params.setdefault("request",self.request)

                        datas=widgets.GetWidgetData(widgetInfo.func,params)

                    #通过sql调用
                    elif widgetInfo.datafrom=="sql":
                        datas=pub.ExecuteSql(widgetInfo.sql)
                        

                    #通过碎片调用
                    elif widgetInfo.datafrom=="block":
                        from UUBlog.apps.blog.views import viewblock
                        datas=viewblock.GetBlockValue(widgetInfo.block)
                        pass

                    #通过url或者html文本
                    elif widgetInfo.datafrom=="url" or widgetInfo.datafrom=="html":
                        datas=tempWidget.datavalues

                    #通过json列表数据
                    elif widgetInfo.datafrom=="json":
                        #datas为list，如：[{"name":"张三","age":30},{"name":"李四","age":30},{"name":"王五","age":30}]
                        datas=utility.Json2Obj(tempWidget.datavalues,[])
                    

                else:
                    #通过url或者html文本
                    if widgetInfo.datafrom=="url" or widgetInfo.datafrom=="html":
                        datas=tempWidget.datavalues

                    #通过json列表数据
                    elif widgetInfo.datafrom=="json":
                        #datas为list，如：[{"name":"张三","age":30},{"name":"李四","age":30},{"name":"王五","age":30}]
                        datas=utility.Json2Obj(tempWidget.datavalues,[])

                widgetValue.setdefault("datas",datas)
                #widgetValue值：{"width":300,"height":500,"title":"我的组件","blogid":4,"datas":[{"name":"张三","age":30},{"name":"李四","age":30}]}
                retWidgetList.append(widgetValue)

        return retWidgetList

  

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























