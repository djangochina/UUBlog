#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect 
from UUBlog.core.ubasetemplateView import UBaseTemplateView

from UUBlog.models import *

from UUBlog.common import utility,pub

from UUBlog.views import widgets

from UUBlog.uu.ubaseblog import UBaseBlogView

class UBaseAdminView(UBaseBlogView):

    
    def __init__(self, **kwargs):
        super(UBaseAdminView, self).__init__(**kwargs)

       

