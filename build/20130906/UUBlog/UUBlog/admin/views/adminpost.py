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

#分类浏览
class PostListView(UBaseAdminView):

    def GetContext(self, **kwargs):
        catid=utility.ToInt(self.GetGetData("catid"),-1)
        istop=utility.ToInt(self.GetGetData("istop"),-1)
        status=utility.ToInt(self.GetGetData("status"),-1)
        time=utility.ToInt(self.GetGetData("time"),-1)
        keywords=self.GetGetData("keywords")


        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)

        postList=Post.objects.order_by("-createtime")

        if catid>-1:
           postList=postList.filter(category_id=catid)
        if istop>-1:
           postList=postList.filter(istop=istop)
        if status>-1:
           postList=postList.filter(status=status)
        if time>-1:
           postList=postList.filter(createtime__gte=datetime.datetime.now()-datetime.timedelta(time))
        if keywords!="":
            postList=postList.filter(title__icontains=keywords)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("admin_pagesize",10)
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList

        self.template_name="admin/postlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('okFilter'):
            catId=self.GetPostData("catTree")
            status=self.GetPostData("status")
            istop=self.GetPostData("istop")
            time=self.GetPostData("time")
            keywords=self.GetPostData("keywords")

            queryString="catid=%s&status=%s&istop=%s&time=%s&keywords=%s" %(catId,status,istop,time,keywords)
            self.returnUrl="/admin/postlist/?"+queryString
            
        return locals()

#文章页面
class PostEditView(UBaseAdminView):

    def GetContext(self, **kwargs):
        action=self.GetGetData("action","edit")
        pid=int(kwargs.get("pid",0))

        if action=="edit":
            catTree="var data=Array();"
            catTree+=self.BuildCatTreeJs(0,-1,-1)

            try:
                postInfo=Post.objects.get(id=pid)
            except:
                postInfo=Post()

            self.template_name="admin/post.html"

        else:
            if action=="delete":
                Post.objects.filter(id=pid).delete()
            self.currentQueryString=self.BuildQueryString(self.currentQueryDic,action=None)
            self.returnUrl="/admin/postlist/"
                

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):

            pid=int(kwargs.get("pid",0))
            catId=utility.ToInt(self.GetPostData("catTree"),0)
            oldCatId=None

            try:
                postInfo=Post.objects.get(id=pid)
                oldCatId=postInfo.category_id
                    
            except:
                postInfo=Post()
            
            
            postInfo.category_id=catId
            
            SetPostValues(self.request,postInfo)

            titlepic=None
            if self.request.FILES.has_key("titlepic"):
                titlepic = self.request.FILES['titlepic']

                #20130711205603+guid
                #201307/11/205603+guid
                currentTime=datetime.datetime.now()
                path="%s/%s/%s/" %("blog/attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
                filename="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())
                
                savedInfo=pub.SaveFile(titlepic,path,filename)
                postInfo.titlepic=savedInfo[0]

            else:
                pics=utility.GetImgSrc(postInfo.content)
                if pics:
                    postInfo.titlepic=pics[0]
                        
            postInfo.save()

            

            if titlepic:
                attachmentInfo=Attachment()
                attachmentInfo.article_id=postInfo.id
                attachmentInfo.user_id=self.currentUser.id
                attachmentInfo.filepath=savedInfo[0]
                attachmentInfo.filename=savedInfo[1]
                attachmentInfo.filetitle=savedInfo[2]
                attachmentInfo.extension=savedInfo[3]
                attachmentInfo.createtime=datetime.datetime.now()

                attachmentInfo.save()

            #更新分类统计信息 不是默认分类并且是发布的文章
            if catId !=0 and postInfo.status:
                categoryInfo=Category.objects.get(id=catId)
                categoryInfo.posts+=1
                categoryInfo.save()
            if oldCatId:

                if oldCatId==catId:
                    pass
                else:

                    pass
                
            else:
                pass
        self.template_name="blog/pub/articleedit.html"

        return locals()

            
def SetPostValues(request,postInfo):
   
    title = pub.GetPostData(request,'title')
    summary=pub.GetPostData(request,'summary')
    content = pub.GetPostData(request,'content')

    tags=pub.GetPostData(request,'tags')
    status = pub.GetPostData(request,'status')
    createtime=pub.GetPostData(request,"createtime")

    cancomment = pub.GetPostData(request,'cancomment')
    istop=pub.GetPostData(request,"istop",False)
    password = pub.GetPostData(request,'password')
    template=pub.GetPostData(request,"template","normal")
    sidebar=pub.GetPostData(request,"sidebar","normal")
   
    if summary=="":
        tempContent=utility.RemoveTags(content)
        summary=tempContent[0:200] if len(tempContent)>200 else tempContent
    else:
        summary=utility.RemoveTags(summary)
   

    postInfo.title = title
    postInfo.tags=tags
    postInfo.summary=summary
    postInfo.content = content
    postInfo.createtime=createtime
    #titlestyle={}
    #titlestyle.setdefault("b",True)     #加粗
    #titlestyle.setdefault("i",True)     #斜体
    #titlestyle.setdefault("u",True)     #下划张
    #titlestyle.setdefault("c",True)     #颜色
    #postInfo.views=0
    #postInfo.comments=0
    #postInfo.goods=0
    #postInfo.bads=0
    postInfo.status=True if status=="1" else False
   
    postInfo.cancomment=cancomment
    postInfo.istop=istop
    postInfo.password=password
    postInfo.user_id=1
    postInfo.username="aaa"
    postInfo.template=template
    postInfo.sidebar=sidebar
  



    
    
    
    
    
    
    
    
    
               