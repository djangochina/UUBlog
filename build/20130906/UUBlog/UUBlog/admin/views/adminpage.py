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

from UUBlog.uu.ubaseadmin import UBaseAdminView



#分类浏览
class PageListView(UBaseAdminView):

    def GetContext(self, **kwargs):
       
        status=int(kwargs.get("status",-1))

        pageList=Page.objects.order_by("-createtime")
      
        if status>-1:
           pageList.filter(status=status)
     

        self.template_name="admin/pagelist.html"

        return locals()



#文章页面
class PageEditView(UBaseAdminView):

    def GetContext(self, **kwargs):
       
        pid=int(kwargs.get("pid",0))
        action=self.GetGetData("action","edit")

        if action=="edit":
            try:
                pageInfo=Page.objects.get(id=pid)
            except:
                pageInfo=Page()
            self.template_name="admin/page.html"

        elif action=="delete":
            Page.objects.filter(id=pid).delete()

        if action!="edit":
            self.returnUrl="/admin/pagelist/"
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):

            pid=int(kwargs.get("pid",0))

            try:
                pageInfo=Page.objects.get(id=pid)
              
            except:
                pageInfo=Page()

          
            SetPageValues(self.request,pageInfo)

            titlepic=None
            if self.request.FILES.has_key("titlepic"):
                titlepic = self.request.FILES['titlepic']

                #20130711205603+guid
                #201307/11/205603+guid
                currentTime=datetime.datetime.now()
                path="%s/%s/%s/" %("blog/attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
                filename="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())
                
                savedInfo=pub.SaveFile(titlepic,path,filename)
                pageInfo.titlepic=savedInfo[0]

            else:
                pics=utility.GetImgSrc(pageInfo.content)
                if pics:
                    pageInfo.titlepic=pics[0]
                        
            pageInfo.save()

            

            if titlepic:
                attachmentInfo=Attachment()
                attachmentInfo.article_id=pageInfo.id
                attachmentInfo.user_id=self.currentUser.id
                attachmentInfo.filepath=savedInfo[0]
                attachmentInfo.filename=savedInfo[1]
                attachmentInfo.filetitle=savedInfo[2]
                attachmentInfo.extension=savedInfo[3]
                attachmentInfo.createtime=datetime.datetime.now()

                attachmentInfo.save()

          
        

        return locals()

            
def SetPageValues(request,pageInfo):
   
    title = pub.GetPostData(request,'title')
    summary=pub.GetPostData(request,'summary')
    content = pub.GetPostData(request,'content')

    status = pub.GetPostData(request,'status')
    cancomment = pub.GetPostData(request,'cancomment')
    password = pub.GetPostData(request,'password')
    template=pub.GetPostData(request,"template","normal")
    sidebar=pub.GetPostData(request,"sidebar","normal")

   
    if summary=="":
        tempContent=utility.RemoveTags(content)
        summary=tempContent[0:200] if len(tempContent)>200 else tempContent
    else:
        summary=utility.RemoveTags(summary)
   

    pageInfo.title = title
    pageInfo.summary=summary
    pageInfo.content = content
    pageInfo.createtime=datetime.datetime.now()
    #titlestyle={}
    #titlestyle.setdefault("b",True)     #加粗
    #titlestyle.setdefault("i",True)     #斜体
    #titlestyle.setdefault("u",True)     #下划张
    #titlestyle.setdefault("c",True)     #颜色
    #pageInfo.views=0
    #pageInfo.comments=0
    #pageInfo.goods=0
    #pageInfo.bads=0
    pageInfo.status=True if status=="1" else False
   
    pageInfo.cancomment=cancomment
    pageInfo.password=password
    pageInfo.user_id=1
    pageInfo.username="aaa"
    pageInfo.template=template
    pageInfo.sidebar=sidebar

  



    
    
    
    
    
    
    
    
    
               