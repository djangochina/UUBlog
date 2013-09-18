#-*- coding:utf-8 -*-


from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","profile")
config.setdefault("title","个人信息")
config.setdefault("description","个人信息")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class ProfileSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(ProfileSetting, self).__init__(**kwargs)
        
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("width",self.GetPostData('width'))
        params.setdefault("height",self.GetPostData('height'))

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')

def ProfileView(uBaseBlog,widget,params,*args,**kwargs):
    return uBaseBlog.user
    

config.setdefault("setting",ProfileSetting)
config.setdefault("view",ProfileView)
