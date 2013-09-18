#-*- coding:utf-8 -*-
import os
import importlib

from UUBlog.settings import ROOT_PATH
from UUBlog.models import Category
from UUBlog.uu.ubaseadmin import UBaseAdminView


class ThemeManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        themeList=[]
        themeDir=os.path.join(ROOT_PATH,'templates','themes')
        dirs=os.listdir(themeDir)
        for dirPath in dirs:
            if dirPath.find(".")>0:
                continue
            themeModuleName="%s.%s.%s" %("UUBlog.templates.themes",dirPath,"config")
            themeList.append(importlib.import_module(themeModuleName).config)

        self.SetTemplateName("themelist")
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            theme=self.GetPostData("theme","default")

            self.UpdateOption("theme",theme)
            
        return locals()

class ThemeEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        categoryInfo=Category.objects.get(id=cid)

        self.SetTemplateName("themelist")
        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()

        return locals()


class HeaderStyleView(UBaseAdminView):

    def GetContext(self, **kwargs):
        
        self.SetTemplateName("headerstyle")
        return locals()

    def PostContext(self, **kwargs):
        uploaded_file = self.GetFile("headerstyle_image")
        if uploaded_file:
            attachInfo=self.SaveFile(uploaded_file)
                      
            self.UpdateOption("headerstyle_image",self.GetPostData("headerstyle_image",attachInfo.path))

        self.UpdateOption("headerstyle_repeat",self.GetPostData("headerstyle_repeat","no-repeat"))
        self.UpdateOption("headerstyle_horizontal",self.GetPostData("headerstyle_horizontal","center"))
        self.UpdateOption("headerstyle_vertical",self.GetPostData("headerstyle_vertical","top"))
        self.UpdateOption("headerstyle_color",self.GetPostData("headerstyle_color","transparent"))
        self.UpdateOption("headerstyle_height",self.GetPostData("headerstyle_height","0"))
        self.UpdateOption("headerstyle_status",self.GetPostData("headerstyle_status","none"))


       
        return locals()

class BackgroundStyleView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        
        self.SetTemplateName("backgroundstyle")
        return locals()

    def PostContext(self, **kwargs):
        uploaded_file = self.GetFile("backgroundstyle_image")
        if uploaded_file:
            attachInfo=self.SaveFile(uploaded_file)
                     
            self.UpdateOption("backgroundstyle_image",self.GetPostData("headerstyle_image",attachInfo.path))

        self.UpdateOption("backgroundstyle_repeat",self.GetPostData("backgroundstyle_repeat","no-repeat"))
        self.UpdateOption("backgroundstyle_horizontal",self.GetPostData("backgroundstyle_horizontal","center"))
        self.UpdateOption("backgroundstyle_vertical",self.GetPostData("backgroundstyle_vertical","top"))
        self.UpdateOption("backgroundstyle_fix",self.GetPostData("backgroundstyle_fix","False"))
        self.UpdateOption("backgroundstyle_color",self.GetPostData("backgroundstyle_color","transparent"))
        self.UpdateOption("backgroundstyle_status",self.GetPostData("backgroundstyle_status","none"))
       
        return locals()




























