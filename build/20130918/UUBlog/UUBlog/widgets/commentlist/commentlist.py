#-*- coding:utf-8 -*-
import datetime
from UUBlog.common import utility
from UUBlog.models import Comment
from UUBlog.uu.ubasewidget import UBaseWidgetView

config={}
config.setdefault("name","commentlist")
config.setdefault("title","评论模块")
config.setdefault("description","评论模块")
config.setdefault("initparams",utility.Obj2Json({"width":400,"height":200}))
config.setdefault("initdata","")


class CommentListSetting(UBaseWidgetView):
    
    def __init__(self,*args, **kwargs):
        super(CommentListSetting, self).__init__(**kwargs)
        self.InitConfig(config)

    def GetWidgetParams(self,**kwargs):
        params={}
        params.setdefault("commentsource",self.GetPostData('commentsource'))
        params.setdefault("orderby",self.GetPostData('orderby'))
        params.setdefault("createtimerange",self.GetPostData('createtimerange'))
        params.setdefault("titlelength",utility.ToInt(self.GetPostData('titlelength'),0))
        params.setdefault("contentlength",utility.ToInt(self.GetPostData('contentlength'),40))
        params.setdefault("count",utility.ToInt(self.GetPostData('count'),10))

        return params

    def GetWidgetData(self,**kwargs):
        return self.GetPostData('data')

def CommentListView(uBaseBlog,widget,params,*args,**kwargs):
    commentsource=utility.GetDicData(params,"commentsource","0")
    orderby=utility.GetDicData(params,"orderby","-createtime")
    createtimerange= utility.ToInt(utility.GetDicData(params,"createtimerange"),0)
    #titlelength=utility.ToInt(utility.GetDicData(params,"titlelength"),40)
    #contentlength=utility.ToInt(utility.GetDicData(params,"contentlength"),40)
    count=utility.ToInt(utility.GetDicData(params,"count"),10)

    commentList=Comment.objects.order_by(orderby)
    if commentsource=="1":
        commentList=commentList.filter(obj_type="post")
    elif commentsource=="2":
        commentList=commentList.filter(obj_type="page")

    if createtimerange>0:
        startTime=datetime.datetime.now()-datetime.timedelta(0,createtimerange)
        commentList=commentList.filter(createtime__gte=startTime)
    return commentList[:count]



config.setdefault("setting",CommentListSetting)
config.setdefault("view",CommentListView)







