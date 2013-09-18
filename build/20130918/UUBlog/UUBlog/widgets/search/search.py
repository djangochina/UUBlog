#-*- coding:utf-8 -*-

from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","search")
config.setdefault("title","搜索")
config.setdefault("description","搜索")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class SearchSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(SearchSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
       

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')

def SearchView(uBaseBlog,widget,params,*args,**kwargs):
    return utility.Json2Obj(widget.data)
        


config.setdefault("setting",SearchSetting)
config.setdefault("view",SearchView)
