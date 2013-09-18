#-*- coding:utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from UUBlog.uu.ubaseblog import UBaseBlogView

class UBaseAdminView(UBaseBlogView):

    
    def __init__(self, **kwargs):
        super(UBaseAdminView, self).__init__(**kwargs)
        self.sidebarList=self.GetSidebarList()
        self.adminTheme="default"
      
    @method_decorator(login_required(login_url="/admin/login/"))
    def dispatch(self, *args, **kwargs):
        return super(UBaseAdminView, self).dispatch(*args, **kwargs) 

    def SetTemplateName(self,templateName):
        self.template_name="admin/%s/%s.html" %(self.adminTheme,templateName)
        #isExists=self.CheckTemplateExists()
        #if isExists==False:
        #    self.message=self.template_name+"模板不存在"
        #    templateName="message"
        #    self.template_name="admin/%s/%s.html" %(self.adminTheme,templateName)