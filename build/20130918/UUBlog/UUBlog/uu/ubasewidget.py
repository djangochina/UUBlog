#-*- coding:utf-8 -*-


from UUBlog.uu.ubaseadmin import UBaseAdminView
from UUBlog.common import utility



class UBaseWidgetView(UBaseAdminView):
   

    def __init__(self, **kwargs):
        super(UBaseAdminView, self).__init__(**kwargs)
        self.name=""
        self.title=""
        self.description=""
        self.params={}
        self.data={}

    def InitConfig(self,config):
        self.name=config["name"]
        self.title=config["title"]
        self.description=config["description"]
        self.params=config["initparams"]
        self.data=config["initdata"]
        
        self.template_name="widgets/%s/%s_setting.html" %(self.name,self.name)



    def GetContext(self,**kwargs):
        wid=int(kwargs.get("wid",0))

        widget=self.GetWidget(wid)

        name=widget.widget
        title=widget.title
        isshowtitle=widget.isshowtitle
        params=utility.Json2Obj(widget.params)
        data=utility.Json2Obj(widget.data,"")

        self.template_name="widgets/%s/%s_setting.html" %(self.name,self.name)
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
        return {}

    def GetWidgetData(self,**kwargs):
        return ""

