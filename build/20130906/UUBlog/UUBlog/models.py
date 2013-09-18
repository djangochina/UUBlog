#-*- coding:utf-8 -*-
import sys 

reload(sys) 
sys.setdefaultencoding("utf-8") 

import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from UUBlog.settings import tablePrefix
from UUBlog.core.ubasemodel import *


class Category(UBaseModel):
    class Meta:
        db_table=tablePrefix+"category"
        verbose_name = "分类管理"
        verbose_name_plural = "分类管理"

    def __unicode__(self):
        return self.name
    
    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    alias=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    posts=models.IntegerField(default=0)
    template=models.CharField(max_length=80)
    sidebar=models.CharField(max_length=80)

class Post(UBaseModel):
    class Meta:
        db_table=tablePrefix+"post"
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"

    category_id=models.IntegerField(default=0)
    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
    tags=models.CharField(max_length=120)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    createtime=models.DateTimeField(default=datetime.datetime.now())
    views=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    status=models.BooleanField(default=True)       #1发布；0草稿
    user_id=models.IntegerField(default=1)
    username=models.CharField(max_length=80)
    istop=models.BooleanField(default=False)            #置顶—1置顶；0否
    cancomment=models.BooleanField(default=True)       
    password=models.CharField(max_length=80)       
    template=models.CharField(max_length=80)
    sidebar=models.CharField(max_length=80)

class Page(UBaseModel):
    class Meta:
        db_table=tablePrefix+"page"
        verbose_name = "页面管理"
        verbose_name_plural = "页面管理"

    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    createtime=models.DateTimeField(default=datetime.datetime.now())
    views=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    status=models.BooleanField(default=True)       #1发布；0草稿
    user_id=models.IntegerField(default=1)
    username=models.CharField(max_length=80)
    cancomment=models.BooleanField(default=True)       
    password=models.CharField(max_length=80)       
    template=models.CharField(max_length=80)
    sidebar=models.CharField(max_length=80)

class Comment(UBaseModel):
    class Meta:
        db_table=tablePrefix+"comment"
        verbose_name = "评论管理"
        verbose_name_plural = "评论管理"
    obj_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    title=models.CharField(max_length=200)
    content=models.TextField()
    createtime=models.DateTimeField(default=datetime.datetime.now())
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    reply_id=models.IntegerField(default=0)
    
class Attachment(UBaseModel):
    class Meta:
        db_table=tablePrefix+"attachment"
        verbose_name = "附件管理"
        verbose_name_plural = "附件管理"
    path=models.CharField(max_length=80)        #attachment/201307/11/163608jc01h66y6cjbc6cf.jpg，年月/日/时分秒32位uuid
    name=models.CharField(max_length=80)        #163608jc01h66y6cjbc6cf.jpg
    title=models.CharField(max_length=80)       #原有的文件名
    description=models.CharField(max_length=200)#文件描述
    extension=models.CharField(max_length=10)       #.jpg、.doc、.mp4
    filetype=models.SmallIntegerField(default=0)    #1：图片；2：多媒体；3：文件,10：其他；
    createtime=models.DateTimeField(default=datetime.datetime.now())

class Sidebar(UBaseModel):
    class Meta:
        db_table=tablePrefix+"sidebar"
        verbose_name = "侧边框"
        verbose_name_plural = "侧边框"
    id=models.CharField(max_length=80,primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

class MyWidget(UBaseModel):
    class Meta:
        db_table=tablePrefix+"mywidget"
        verbose_name = "我的Widget管理"
        verbose_name_plural = "我的Widget管理"
    def __unicode__(self):
        return self.title
    sidebar_id=models.CharField(max_length=80)
    widget=models.CharField(max_length=80)
    title=models.CharField(max_length=80)
    isshowtitle=models.BooleanField(default=False)     
    params=models.CharField(max_length=2000)   
    data=models.CharField(max_length=2000)       
    sortnum=models.IntegerField(default=0)

class Navigate(UBaseModel):
    class Meta:
        db_table=tablePrefix+"navigate"
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
    description=models.CharField(max_length=80,null=True,blank=True,default="")        #属性定义
    position=models.SmallIntegerField(choices=POSITION_CHOICES,default=1)        
    align=models.SmallIntegerField(default=1,choices=ALIGN_CHOICES)
    url=models.CharField(max_length=200,null=True,blank=True)           #函数名
    target=models.CharField(max_length=20,choices=TARGET_CHOICES,default="_self")         #参数
    fontstyle=models.CharField(max_length=200,null=True,blank=True,default="")            #sql语句
    sortnum=models.IntegerField(default=0)          #显示顺序

class Option(UBaseModel):
    class Meta:
        db_table=tablePrefix+"option"
        verbose_name = "设置"
        verbose_name_plural = "设置"

    name=models.CharField(max_length=80)        
    value=models.CharField(max_length=2000)    
   


   












