#-*- coding:utf-8 -*-

from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView

from UUBlog.models import *

from UUBlog.common import utility,pub



class UBaseWidgetView(UBaseTemplateView):
   

    def __init__(self, **kwargs):
        super(UBaseWidgetView, self).__init__(**kwargs)
        self.name=""
        self.title=""
        self.description=""
        self.params={}
        self.data={}


    def InitValue(self,config):
        self.name=config["name"]
        self.title=config["title"]
        self.description=config["description"]
        self.params=config["initparams"]
        self.data=config["initdata"]
        
        self.template_name="widgets/"+self.name+"_setting.html"

    def post_context_data(self, **kwargs):
        context= super(UBaseWidgetView, self).post_context_data(**kwargs)
       
        myContext=self.PostContext(**kwargs)
        
        self.AddVars(context,myContext)

        self.AddVars(context,locals())

        return context


    def get_context_data(self, **kwargs):
        context= super(UBaseWidgetView, self).get_context_data(**kwargs)

        myContext=self.GetContext(**kwargs)

        self.AddVars(context,myContext)

        self.AddVars(context,locals())

        return context

    def GetContext(self,**kwargs):
        wid=int(kwargs.get("wid",0))

        widget=self.GetWidget(wid)

        title=widget.title
        isshowtitle=widget.isshowtitle
        params=utility.Json2Obj(widget.params)
        data=utility.Json2Obj(widget.data,"")

        self.template_name="widgets/"+self.name+"_setting.html"
        return locals()

    def PostContext(self, **kwargs):
        wid=int(kwargs.get("wid",0))

        if self.HasPostData("ok"):

            widget=self.GetWidget(wid)

            widget.title = self.GetPostData('title')
            widget.isshowtitle=self.GetPostData('isshowtitle',False)
            widget.params=utility.Obj2Json(self.GetWidgetParams(**kwargs))
            widget.data=utility.Obj2Json(self.GetWidgetData(**kwargs))

            widget.save()
    
    def GetWidgetParams(self,**kwargs):
        return ""

    def GetWidgetData(self,**kwargs):
        return ""

    def GetWidget(self,wid):
        widget=MyWidget.objects.get(id=wid)
        return widget
