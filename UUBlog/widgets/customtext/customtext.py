#-*- coding:utf-8 -*-


from UUBlog.common import utility
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","customtext")
config.setdefault("title","自定义文本")
config.setdefault("description","自定义文本")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")


class CustomTextSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(CustomTextSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
     
        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('textContent')

def CustomTextView(uBaseBlog,widget,params,*args,**kwargs):
    return utility.Json2Obj(widget.data)

   



config.setdefault("setting",CustomTextSetting)
config.setdefault("view",CustomTextView)







