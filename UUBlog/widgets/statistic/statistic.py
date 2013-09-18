#-*- coding:utf-8 -*-

from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","statistic")
config.setdefault("title","统计信息")
config.setdefault("description","统计信息")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class StatisticSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(StatisticSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("width",self.GetPostData('width'))
        params.setdefault("height",self.GetPostData('height'))

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')

def StatisticView(uBaseBlog,widget,params,*args,**kwargs):
    return uBaseBlog.user
    


config.setdefault("setting",StatisticSetting)
config.setdefault("view",StatisticView)

