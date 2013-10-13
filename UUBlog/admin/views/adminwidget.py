#-*- coding:utf-8 -*-



from UUBlog.common import utility, pub
from UUBlog.models import Sidebar, MyWidget
from UUBlog.uu.ubaseblog import G
from UUBlog.uu.ubaseadmin import UBaseAdminView


class WidgetManagerView(UBaseAdminView):
    def DefaultTemplateName(self):
        return "widgetlist"

    def GetContext(self, **kwargs):

        global G

        widgetList = G["widgets"]

        sid = utility.GetDicData(kwargs, "sid")

        sidebarInfo = Sidebar.objects.get(id=sid)

        myWidgetList = self.GetWidgetList(sid, False)

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            global G
            sid = kwargs.get("sid", 0)
            widgets = self.GetRequestListData("widget")
            
            for widgetName in widgets:

                widgetModule=G["widgets"][widgetName]

                myWidget = MyWidget()
                myWidget.sidebar_id = sid
                myWidget.widget = widgetModule.config["name"]
                myWidget.title = widgetModule.config["title"]
                myWidget.isshowtitle = True
                myWidget.params = widgetModule.config["initparams"]
                myWidget.data = widgetModule.config["initdata"]
                myWidget.sortnum = 0

                myWidget.save()

        if self.HasPostData("okSort"):
            for key, value in self.request.POST.items():
                if key.find("item_sortnum_") == 0:
                    dot = key.rfind("_")
                    myWId = key[dot+1:]
                    MyWidget.objects.filter(id=myWId).update(sortnum=utility.ToInt(value, 0))

        self.reload = True
        return locals()

def WidgetSettingView(request, wid):
    myWidget = MyWidget.objects.get(id=wid)

    global G
    widgetModule = G["widgets"][myWidget.widget]

    widgetSetting = widgetModule.config["setting"]

    return widgetSetting.as_view()(request, wid=wid)



class WidgetEditView(UBaseAdminView):
    
    def DefaultTemplateName(self):
        return "widget"

    def GetContext(self, **kwargs):
        sid = utility.GetDicData(kwargs, "sid")

        wid = utility.ToInt(utility.GetDicData(kwargs, "wid"), 0)
        
        action = self.GetGetData("action", "edit")
        if action == "edit":
            widgetInfo = MyWidget.objects.get(id=wid)
        else:
            if action == "delete":
                MyWidget.objects.filter(id=wid).delete()
            self.redirectUrl = "/admin/widgetlist/%s/" % sid
            self.currentQueryString = self.BuildQueryString(action=None)

        return locals()

    def PostContext(self, **kwargs):
        
        return locals()





























