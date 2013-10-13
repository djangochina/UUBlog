#-*- coding:utf-8 -*-
from UUBlog.uu.ubaseblog import UBaseBlogView


class UBaseUserView(UBaseBlogView):

    def __init__(self, **kwargs):
        super(UBaseUserView, self).__init__(**kwargs)
        self.navs = {}

    def InitValue(self):
        super(UBaseUserView, self).InitValue()
        self.navs = {}
        self.navs["main"] = self.BuildNavTreeHtml(0)
        self.navs["top"] = {}
        self.navs["top"]["left"] = self.GetNavList(position=2, align=1)
        self.navs["top"]["right"] = self.GetNavList(position=2, align=3)
        self.navs["bottom"] = self.GetNavList(position=3)
        
        self.templateName = "normal"
        self.sidebar = "normal"
        self.sidebarFloat = "none"

    def SetTemplateName(self, templateName):
        self.template_name = "themes/%s/%s.html" % (self.theme, templateName)
        #isExists=self.CheckTemplateExists()
        #if isExists==False:
        #    self.message=self.template_name

        #    dot=templateName.find("_")
        #    templateName=templateName[0:dot+1]+"normal"
        #    self.template_name="themes/%s/%s.html" %(self.theme,templateName)

        #    isExists=self.CheckTemplateExists()
        #    if isExists==False:
        #        self.message+=self.template_name+"不存在"
        #        templateName="message"
        #        self.template_name="themes/%s/%s.html" %(self.theme,templateName)

    def SetTemplateAndSidebar(self, **kwargs):
        self.widgetList = self.GetWidgetList(self.sidebar)
        self.SetTemplateName(self.templateName)

    def SetMessageTemplate(self, messageInfo = None):
        if messageInfo is None or messageInfo == "":
            messageInfo = "发生未知错误"
        self.message = messageInfo
        
        self.templateName = "message"
        self.sidebar = self.GetOption("message_sidebar", "normal")
        self.sidebarFloat = self.GetOption("message_sidebar_float", "none")

        self.SetTemplateAndSidebar()

    def GetContext(self, **kwargs):
        close_site = self.GetOption("close_site", "True")
        if close_site == "True" and self.__class__.__name__ != "CloseView":
            self.redirectUrl = "/close/"
        else:
            return super(UBaseUserView, self).GetContext(**kwargs)

   

        

        