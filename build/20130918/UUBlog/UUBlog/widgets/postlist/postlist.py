#-*- coding:utf-8 -*-
import datetime

from UUBlog.common import utility
from UUBlog.models import Post
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","postlist")
config.setdefault("title","文章模块")
config.setdefault("description","文章模块")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")

class PostListSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(PostListSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("keywords",self.GetPostData('keywords'))
        params.setdefault("orderby",self.GetPostData('orderby'))
        params.setdefault("createtimerange",self.GetPostData('createtimerange'))
        params.setdefault("titlelength",utility.ToInt(self.GetPostData('titlelength')))
        params.setdefault("count",utility.ToInt(self.GetPostData('count'),10))

        return params

    def GetWidgetData(self,**kwargs):
        return ""

def PostListView(uBaseBlog,widget,params,*args,**kwargs):
    keywords=utility.GetDicData(params,"keywords","keywords")
    orderby=utility.GetDicData(params,"orderby","-createtime")
    createtimerange= utility.ToInt(utility.GetDicData(params,"createtimerange"),0)
    #titlelength=utility.ToInt(utility.GetDicData(params,"titlelength"),40)
    count=utility.ToInt(utility.GetDicData(params,"count"),10)

    postList=Post.objects.order_by(orderby).filter(status=1)
    if keywords!="":
        postList=postList.filter(title__icontains=keywords)
    if createtimerange>0:
        startTime=datetime.datetime.now()-datetime.timedelta(0,createtimerange)
        postList=postList.filter(createtime__gte=startTime)
    return postList[:count]



config.setdefault("setting",PostListSetting)
config.setdefault("view",PostListView)

