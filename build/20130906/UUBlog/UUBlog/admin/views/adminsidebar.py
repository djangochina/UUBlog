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


class SidebarManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        mySidebarList=Sidebar.objects.all()

        self.template_name="admin/sidebarlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            sidebarInfo=Sidebar()

            sidebarInfo.id=self.GetPostData("id")
            sidebarInfo.name=self.GetPostData("name")
            sidebarInfo.description=self.GetPostData("description",sidebarInfo.name)

            sidebarInfo.save()

        return locals()

class SidebarEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        sid=kwargs.get("sid")
        
        action=self.GetGetData("action","edit")
        if action=="edit":

            sidebarInfo=Sidebar.objects.get(id=sid)
        
            self.template_name="admin/sidebar.html"
        elif action=="delete":
            Sidebar.objects.filter(id=sid).delete()
            MyWidget.objects.filter(sidebar_id=sid).delete()

        if action!="edit":
            self.returnUrl="/admin/sidebarlist/"
        

        return locals()

    def PostContext(self, **kwargs):
        sid=kwargs.get("sid")

        if self.HasPostData('ok'):

            sidebarInfo=Sidebar(id=sid)
            sidebarInfo.name=self.GetPostData("name")
            sidebarInfo.description=self.GetPostData("description")

            sidebarInfo.save()
        self.returnUrl="/admin/sidebarlist/"
        return locals()

class WidgetManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        global G

        widgetList=G["widgets"]

        sid=utility.GetDicData(kwargs,"sid")

        sidebarInfo=Sidebar.objects.get(id=sid)

        myWidgetList=self.GetWidgetList(sid,False)

        self.template_name="admin/widgetlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            global G
            sid=kwargs.get("sid",0)
            widgets=self.GetRequestListData("widget")
            
            for widgetName in widgets:

                widgetModule=G["widgets"][widgetName]

                myWidget=MyWidget()
                myWidget.sidebar_id=sid
                myWidget.widget=widgetModule.config["name"]
                myWidget.title=widgetModule.config["title"]
                myWidget.isshowtitle=True
                myWidget.params=widgetModule.config["initparams"]
                myWidget.data=widgetModule.config["initdata"]
                myWidget.sortnum=0

                myWidget.save()

        if self.HasPostData("okSort"):
            for key,value in self.request.POST.items():
                if key.find("item_sortnum_")==0:
                    dot=key.rfind("_")
                    myWId=key[dot+1:]
                    MyWidget.objects.filter(id=myWId).update(sortnum=utility.ToInt(value,0))

        return locals()

class WidgetEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        sid=utility.GetDicData(kwargs,"sid")

        wid=utility.ToInt(utility.GetDicData(kwargs,"wid"),0)
        
        action=self.GetGetData("action","edit")
        if action=="edit":
            widgetInfo=MyWidget.objects.get(id=wid)

            self.template_name="admin/widget.html"
        elif action=="delete":
            MyWidget.objects.filter(id=wid).delete()
        
        self.returnUrl="/admin/widgetlist/%s/" %sid

        return locals()

    def PostContext(self, **kwargs):
        
        return locals()





























