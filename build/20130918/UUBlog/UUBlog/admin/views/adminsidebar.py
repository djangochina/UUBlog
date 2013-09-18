#-*- coding:utf-8 -*-



from UUBlog.common import utility
from UUBlog.models import Sidebar,MyWidget
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


class WidgetManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        
        global G

        widgetList=G["widgets"]

        sid=utility.GetDicData(kwargs,"sid")

        sidebarInfo=Sidebar.objects.get(id=sid)

        myWidgetList=self.GetWidgetList(sid,False)

        self.SetTemplateName("widgetlist")
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
            self.SetTemplateName("widget")
        elif action=="delete":
            MyWidget.objects.filter(id=wid).delete()
        
        self.redirectUrl="/admin/widgetlist/%s/" %sid

        return locals()

    def PostContext(self, **kwargs):
        
        return locals()





























