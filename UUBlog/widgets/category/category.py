#-*- coding:utf-8 -*-

from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","category")
config.setdefault("title","分类")
config.setdefault("description","分类")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class CategorySetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(CategorySetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("width",self.GetPostData('width'))
        params.setdefault("height",self.GetPostData('height'))

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')


def CategoryView(uBaseBlog,widget,params,*args,**kwargs):
    catTreeHtml=uBaseBlog.BuildCatTreeHtml(0,-1)

    #categoryList=Category.objects.order_by("-sortnum").all()

    return catTreeHtml



config.setdefault("setting",CategorySetting)
config.setdefault("view",CategoryView)




