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
        uid=int(kwargs.get("uid",0))

        myWidgetList=self.GetMyWidgetList()
       
        postList=self.GetPostList(uid)
      
        #更新博客访客
        self.AddVisit(uid)

        self.template_name="admin/index.html"

        return locals()

#分类浏览
class PostListView(UBaseAdminView):

    def GetContext(self, **kwargs):
        cid=int(kwargs.get("cid",-1))
        tid=int(kwargs.get("tid",-1))
        status=int(kwargs.get("status",-1))

        postList=Post.objects.order_by("-createtime")

        if cid>-1:
           postList.filter(categor_id=cid)
        if tid>-1:
           postList.filter(tag_id=tid)

        if status>-1:
           postList.filter(status=status)
     

        self.template_name="admin/postlist.html"

        return locals()



#文章页面
class PostView(UBaseAdminView):

    def GetContext(self, **kwargs):
        pid=int(kwargs.get("pid",0))

        try:
            postInfo=Post.objects.get(id=pid)
            hookList=self.GetHookList("post_BeforShow")
            for hook in hookList:
                if callable(hook):
                    postInfo=hook(postInfo)

        except:
            postInfo=Post()

        

        self.template_name="admin/post.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            
            

            category=Category.objects.get(id=self.GetPostData('category'))

            articleInfo=Article()
            articleInfo.category=category
            articleInfo.createtime=datetime.datetime.now()
            articleInfo.user_id=self.currentUser.id
            articleInfo.username=self.currentUser.username
            SetArticleValues(self.request,articleInfo)

            titlepic=None
            if self.request.FILES.has_key("titlepic"):
                titlepic = self.request.FILES['titlepic']

            if titlepic:
                #20130711205603+guid
                #201307/11/205603+guid
                currentTime=datetime.datetime.now()
                path="%s/%s/%s/" %("blog/attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
                filename="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())
                
                savedInfo=pub.SaveFile(titlepic,path,filename)
                articleInfo.titlepic=savedInfo[0]

            else:
                pics=utility.GetImgSrc(articleInfo.content)
                if pics:
                    articleInfo.titlepic=pics[0]
                        
            articleInfo.save()

            titlestyle={}
            titlestyle.setdefault("b",True)     #加粗
            titlestyle.setdefault("i",True)     #斜体
            titlestyle.setdefault("u",True)     #下划张
            titlestyle.setdefault("c",True)     #颜色

            if titlepic:
                attachmentInfo=Attachment()
                attachmentInfo.article_id=articleInfo.id
                attachmentInfo.user_id=self.currentUser.id
                attachmentInfo.filepath=savedInfo[0]
                attachmentInfo.filename=savedInfo[1]
                attachmentInfo.filetitle=savedInfo[2]
                attachmentInfo.extension=savedInfo[3]
                attachmentInfo.createtime=datetime.datetime.now()

                attachmentInfo.save()

            #更新分类统计信息 不是默认分类并且是发布的文章
            if category.id !=1 and articleInfo.status:
                category.articles+=1
                category.save()

        self.template_name="blog/pub/articleedit.html"

        return locals()

            
def SetArticleValues(request,articleInfo):
   
    title = pub.GetPostData(request,'title')
    summary=pub.GetPostData(request,'summary')
    content = pub.GetPostData(request,'content')

    tags=pub.GetPostData(request,'tags')
    status = pub.GetPostData(request,'status')
    cancomment = pub.GetPostData(request,'cancomment')
    password = pub.GetPostData(request,'password')

   
    if summary=="":
        tempContent=utility.RemoveTags(content)
        summary=tempContent[0:200] if len(tempContent)>200 else tempContent
    else:
        summary=utility.RemoveTags(summary)
   

    articleInfo.title = title
    articleInfo.tags=tags
    articleInfo.summary=summary
    articleInfo.content = content
    #articleInfo.createtime=datetime.datetime.now()

    #articleInfo.views=0
    #articleInfo.comments=0
    #articleInfo.goods=0
    #articleInfo.bads=0
    articleInfo.status=status
   
    articleInfo.cancomment=cancomment
    articleInfo.password=password

  



    
    
    
    
    
    
    
    
    
               