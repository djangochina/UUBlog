#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from UUBlog.models import *

from UUBlog.common import utility,pub

from UUBlog.uu.ubaseblog import UBaseBlogView

class UBaseAdminView(UBaseBlogView):

    
    def __init__(self, **kwargs):
        super(UBaseAdminView, self).__init__(**kwargs)
        self.sidebarList=self.GetSidebarList()
      
    @method_decorator(login_required(login_url="/admin/login/"))
    def dispatch(self, *args, **kwargs):
        return super(UBaseAdminView, self).dispatch(*args, **kwargs) 

