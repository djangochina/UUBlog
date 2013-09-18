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


class CatManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)

        catList=self.GetCatList()

        self.template_name="admin/catlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias",name)
            sortnum=utility.ToInt(self.GetPostData("sortnum"))
            template=self.GetPostData("template","normal")
            sidebar=self.GetPostData("sidebar","normal")

            catInfo=Category()
            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0
            catInfo.template=template
            catInfo.sidebar=sidebar

            catInfo.save()
        if self.HasPostData("okSort"):
            for key,value in self.request.POST.items():
                if key.find("item_sortnum_")==0:
                    dot=key.rfind("_")
                    catId=key[dot+1:]
                    Category.objects.filter(id=catId).update(sortnum=utility.ToInt(value,0))
        return locals()

class CatEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        cid=int(kwargs.get("cid",0))
        catInfo=Category.objects.get(id=cid)

        action=self.GetGetData("action","edit")

        if action=="edit":

            catTree="var data=Array();"
            catTree+=self.BuildCatTreeJs(0,-1,cid)
            self.template_name="admin/cat.html"
        elif action=="delete":
            Category.objects.filter(id=cid).delete()
            Category.objects.filter(parent_id=cid).update(parent_id=catInfo.parent_id)

        if action!="edit":
            self.returnUrl="/admin/catlist/"

        return locals()

    def PostContext(self, **kwargs):
       
        if self.HasPostData('ok'):
            cid=int(kwargs.get("cid",0))
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            sortnum=self.GetPostData("sortnum",0)
            template=self.GetPostData("template","normal")
            sidebar=self.GetPostData("sidebar","normal")

            catInfo=Category.objects.get(id=cid)
            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0
            catInfo.template=template
            catInfo.sidebar=sidebar

            catInfo.save()
        
        self.returnUrl="/admin/catlist"
        return locals()




    