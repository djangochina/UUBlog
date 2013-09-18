#-*- coding:utf-8 -*-


from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","cp")
config.setdefault("title","控制面板")
config.setdefault("description","控制面板")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class CPSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(CPSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
       

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')

def CPView(uBaseBlog,widget,params,*args,**kwargs):
    return uBaseBlog.user
    

config.setdefault("setting",CPSetting)
config.setdefault("view",CPView)

