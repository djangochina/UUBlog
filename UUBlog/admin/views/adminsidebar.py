#-*- coding:utf-8 -*-



from UUBlog.common import utility, pub
from UUBlog.models import Sidebar, MyWidget
from UUBlog.uu.ubaseblog import G
from UUBlog.uu.ubaseadmin import UBaseAdminView



class SidebarManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        mySidebarList=Sidebar.objects.all()

        self.SetTemplateName("sidebarlist")
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
        
            self.SetTemplateName("sidebar")
        elif action=="delete":
            Sidebar.objects.filter(id=sid).delete()
            MyWidget.objects.filter(sidebar_id=sid).delete()

        if action!="edit":
            self.redirectUrl="/admin/sidebarlist/"
        

        return locals()

    def PostContext(self, **kwargs):
        sid=kwargs.get("sid")

        if self.HasPostData('ok'):

            sidebarInfo=Sidebar(id=sid)
            sidebarInfo.name=self.GetPostData("name")
            sidebarInfo.description=self.GetPostData("description")

            sidebarInfo.save()
        self.redirectUrl="/admin/sidebarlist/"
        return locals()






























