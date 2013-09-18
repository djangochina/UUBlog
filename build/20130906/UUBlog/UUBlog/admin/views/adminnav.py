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
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from UUBlog.common import pub,utility
from UUBlog.models import *
from UUBlog.uu.ubaseadmin import UBaseAdminView

from UUBlog.init import *



class NavManagerView(UBaseAdminView):

    def GetContext(self, **kwargs):

        position=int(utility.GetDicData(kwargs,"p",'1'))

        #菜单树
        navTree="var data=Array();"
        navTree+=self.BuildNavTreeJs(0,position,-1,-1)

        #分类树
        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)
        
        pageList=self.GetPageList()

        self.template_name="admin/navlist.html"

        return locals()

    def PostContext(self, **kwargs):
        position=utility.GetDicData(kwargs,"p",1)

        if self.HasPostData('okUrl'):

            parent_id=self.GetPostData("parentId",0)
            name=self.GetPostData("name")            
            url=self.GetPostData("url","#")
            align=self.GetPostData("align",1)
           
            navInfo=Navigate(parent_id=parent_id,position=position,name=name,url=url,alias=name)
            navInfo.align=align
            navInfo.save()

        if self.HasPostData("okCat"):
            catIds=self.GetRequestListData("catTree")
            for catId in catIds:
                catInfo=Category.objects.get(id=catId)

                navInfo=Navigate(parent_id=0,position=position)
                navInfo.name=catInfo.name
                navInfo.alias=catInfo.name
                navInfo.url="/cat/%s/" %catId

                navInfo.save()

        if self.HasPostData("okPage"):
            pageIds=self.GetRequestListData("page")
            for pageId in pageIds:
                pageInfo=Page.objects.get(id=pageId)

                navInfo=Navigate(parent_id=0,position=position)
                navInfo.name=pageInfo.title
                navInfo.alias=pageInfo.title
                navInfo.url="/page/%s/" %pageId

                navInfo.save()

        if self.HasPostData("okSort"):
            for key,value in self.request.POST.items():
                if key.find("item_sortnum_")==0:
                    dot=key.rfind("_")
                    navId=key[dot+1:]
                    Navigate.objects.filter(id=navId).update(sortnum=utility.ToInt(value,0))

        self.returnUrl="/admin/navlist/position/%s/" %position

        return locals()

class NavEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        position=utility.ToInt(utility.GetDicData(kwargs,"p"),1)
        nid=utility.ToInt(utility.GetDicData(kwargs,"nid"))

        navInfo=Navigate.objects.get(id=nid)

        action=self.GetGetData("action","edit")
        if action=="edit":
            navTree="var data=Array();"
            navTree+=self.BuildNavTreeJs(0,position,-1,nid)
       
            

            self.template_name="admin/nav.html"
        elif action=="delete":
            Navigate.objects.filter(id=nid).delete()
            Navigate.objects.filter(parent_id=nid).update(parent_id=navInfo.parent_id)
        
        if action != "edit":
            self.returnUrl="/admin/navlist/position/%s/" %position

        return locals()

    def PostContext(self, **kwargs):
        
        if self.HasPostData('ok'):
            
            position=utility.ToInt(utility.GetDicData(kwargs,"p"),1)
            nid=utility.ToInt(utility.GetDicData(kwargs,"nid"),None)

            parent_id=utility.ToInt(self.GetPostData("parentId"),0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            description=self.GetPostData("description")
            
            align=utility.ToInt(self.GetPostData("align"),1)
            url=self.GetPostData("url","#")
            target=self.GetPostData("target")
            fontstyle=self.GetPostData("fontstyle")
            isenable=self.GetPostData("isenable",0)
            sortnum=utility.ToInt(self.GetPostData("sortnum"),0)
           
            navInfo=Navigate()

            if nid:
                try:
                    navInfo=Navigate.objects.get(id=nid)
                except:
                    pass
            
            navInfo.parent_id=parent_id
            navInfo.name=name
            navInfo.name=name
            navInfo.alias=alias
            navInfo.description=description
            navInfo.position=position
            navInfo.align=align
            navInfo.url=url
            navInfo.target=target
            navInfo.fontstyle=fontstyle
            navInfo.isenable=isenable
            navInfo.sortnum=0 if sortnum=="" else int(sortnum)

            navInfo.save()

            self.returnUrl="/admin/navlist/position/%s/" %position
        return locals()



























