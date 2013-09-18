#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView

from UUBlog.models import *

from UUBlog.common import utility,pub

from UUBlog.uu.ubaseblog import UBaseBlogView

class UBaseUserView(UBaseBlogView):

    
    def __init__(self, **kwargs):
        super(UBaseUserView, self).__init__(**kwargs)

    def InitValue(self):
        super(UBaseUserView, self).InitValue()
        self.sidebar="normal"
        self.templateName="normal"

    def SetTemplateAndSidebar(self, **kwargs):
        self.widgetList=self.GetWidgetList(self.sidebar)
        self.SetTemplateName(self.templateName)

    def GetContext(self, **kwargs):
        close_site=utility.GetDicData(self.options,"close_site","True")
        close_info=utility.GetDicData(self.options,"close_info","")
        if close_site=="True":
            self.returnUrl="/admin/"
        else:
            return super(UBaseUserView, self).GetContext(**kwargs)

   

        

        