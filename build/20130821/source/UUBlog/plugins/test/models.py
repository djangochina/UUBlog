#-*- coding:utf-8 -*-
import sys 

reload(sys) 
sys.setdefaultencoding("utf-8") 

import datetime
from UUBlog.core.ubasemodel import *
from django.utils import timezone
from django.contrib.auth.models import User

class Category(UBaseModel):
    class Meta:
        db_table="uublog_category"
    def __unicode__(self):
        return self.name

    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    alias=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    
class Post(UBaseModel):
    class Meta:
        db_table="uublog_post"
    category=models.ForeignKey(Category)
    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
    tags=models.CharField(max_length=120)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    createtime=models.DateTimeField(default="0000-00-00 00:00:00")
    views=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    status=models.BooleanField(default=True)       #1发布；0草稿
    user_id=models.IntegerField(default=1)
    username=models.CharField(max_length=80)
    istop=models.BooleanField(default=False)            #置顶—1置顶；0否
    isoriginal=models.BooleanField(default=True)       #原创—1原创；0否
    cancomment=models.BooleanField(default=True)       
    password=models.CharField(max_length=80)       
    ishome=models.BooleanField(default=False)           #首页—1发布到首页；0否
    isrecommend=models.BooleanField(default=False)      #推荐—1推荐；0否


class Comment(UBaseModel):
    class Meta:
        db_table="uublog_comment"
    post=models.ForeignKey(Post)
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=80)
    content=models.TextField()
    createtime=models.DateTimeField(default="0000-00-00 00:00:00")
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    reply_id=models.IntegerField(default=0)
    

class Attachment(UBaseModel):
    class Meta:
        db_table="uublog_attachment"
    post_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    filepath=models.CharField(max_length=80)        #blog/attachment/201307/11/163608jc01h66y6cjbc6cf.jpg，年月/日/时分秒32位guid
    filename=models.CharField(max_length=80)    #163608jc01h66y6cjbc6cf.jpg
    filetitle=models.CharField(max_length=80)    #原有的文件名
    extension=models.CharField(max_length=10)   #jpg
    createtime=models.DateTimeField(default=datetime.datetime.now())


class Widget(UBaseModel):
    class Meta:
        db_table="uublog_widget"
        verbose_name = "Widget管理"
        verbose_name_plural = "Widget管理"
    def __unicode__(self):
        return self.title

    DATAFROM_CHOICES = (
        ("func", "函数调用"),
        ("sql", "sql调用"),
        ("url", "Url地址"),
        ("html", "文本录入"),
        ("json", "json列表数据录入"),
    )
    
    name=models.CharField(max_length=80,primary_key=True)        #blog/attachment/201307/11/163608jc01h66y6cjbc6cf.jpg，年月/日/时分秒32位guid
    title=models.CharField(max_length=80)    #163608jc01h66y6cjbc6cf.jpg
    attdef=models.CharField(max_length=2000,null=True,blank=True)        #属性定义
    datafrom=models.CharField(max_length=20,choices=DATAFROM_CHOICES)        #func、sql、block、url、html、json
    func=models.CharField(max_length=256,null=True,blank=True)           #函数名
    params=models.CharField(max_length=500,null=True,blank=True)         #参数
    sql=models.CharField(max_length=256,null=True,blank=True)            #sql语句
    defaultdata=models.CharField(max_length=256,null=True,blank=True)    #默认数据
    jsondef=models.CharField(max_length=2000,null=True,blank=True)       #datafrom为json时，定义json的对象
    canedit=models.BooleanField(default=False)          #是否可编辑默认数据
    render=models.CharField(max_length=2000)        #render模板代码
    issys=models.BooleanField(default=False)            #是否是系统widget
    sortnum=models.IntegerField(default=0)          #显示顺序

class MyWidget(UBaseModel):
    class Meta:
        db_table="uublog_mywidget"
    def __unicode__(self):
        return self.title

    widget=models.ForeignKey(Widget)
    title=models.CharField(max_length=80)  
    params=models.CharField(max_length=2000)   
    attvalues=models.CharField(max_length=2000)
    datavalues=models.CharField(max_length=2000)       
    sortnum=models.IntegerField(default=0)



class Navigate(UBaseModel):
    class Meta:
        db_table="uublog_navigate"
        verbose_name = "导航管理"
        verbose_name_plural = "导航管理"
    def __unicode__(self):
        return self.alias
    POSITION_CHOICES = (
        (1, "主导航"),
        (2, "顶部导航"),
        (3, "底部导航"),
    )

    ALIGN_CHOICES = (
        (1, "左"),
        (2, "中"),
        (3, "右"),
    )

    TARGET_CHOICES = (
        ("_self", "当前窗口"),
        ("_blank", "新窗口"),
    )

    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)        
    alias=models.CharField(max_length=80)    
    description=models.CharField(max_length=80,null=True,blank=True)        #属性定义
    position=models.SmallIntegerField(default=1,choices=POSITION_CHOICES)        
    align=models.SmallIntegerField(default=1,choices=ALIGN_CHOICES)
    url=models.CharField(max_length=200,null=True,blank=True)           #函数名
    target=models.CharField(max_length=20,choices=TARGET_CHOICES,default="_self")         #参数
    fontstyle=models.CharField(max_length=200,null=True,blank=True)            #sql语句
    isenable=models.BooleanField(default=True)            #是否是系统widget
    sortnum=models.IntegerField(default=0)          #显示顺序




