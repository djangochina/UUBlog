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
        verbose_name = "分类管理"
        verbose_name_plural = "分类管理"
    def __unicode__(self):
        return self.name

    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    alias=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    posts=models.IntegerField(default=0)
    
class Post(UBaseModel):
    class Meta:
        db_table="uublog_post"
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"

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
    cancomment=models.BooleanField(default=True)       
    password=models.CharField(max_length=80)       


class Comment(UBaseModel):
    class Meta:
        db_table="uublog_comment"
        verbose_name = "评论管理"
        verbose_name_plural = "评论管理"
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
        verbose_name = "附件管理"
        verbose_name_plural = "附件管理"
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
        verbose_name = "所有Widget管理"
        verbose_name_plural = "所有Widget管理"
    def __unicode__(self):
        return self.title

    
    name=models.CharField(max_length=80,primary_key=True)        #blog/attachment/201307/11/163608jc01h66y6cjbc6cf.jpg，年月/日/时分秒32位guid
    title=models.CharField(max_length=80)    #163608jc01h66y6cjbc6cf.jpg
    params=models.CharField(max_length=2000,null=True,blank=True)         #参数
    data=models.CharField(max_length=2000,null=True,blank=True)    #默认数据

class MyWidget(UBaseModel):
    class Meta:
        db_table="uublog_mywidget"
        verbose_name = "我的Widget管理"
        verbose_name_plural = "我的Widget管理"
    def __unicode__(self):
        return self.title

    widget=models.CharField(max_length=80)
    title=models.CharField(max_length=80)
    isshowtitle=models.BooleanField(default=False)     
    params=models.CharField(max_length=2000)   
    data=models.CharField(max_length=2000)       
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
    description=models.CharField(max_length=80,null=True,blank=True,default="")        #属性定义
    position=models.SmallIntegerField(choices=POSITION_CHOICES,default=1)        
    align=models.SmallIntegerField(default=1,choices=ALIGN_CHOICES)
    url=models.CharField(max_length=200,null=True,blank=True)           #函数名
    target=models.CharField(max_length=20,choices=TARGET_CHOICES,default="_self")         #参数
    fontstyle=models.CharField(max_length=200,null=True,blank=True,default="")            #sql语句
    sortnum=models.IntegerField(default=0)          #显示顺序




class Option(UBaseModel):
    class Meta:
        db_table="uublog_option"
        verbose_name = "设置"
        verbose_name_plural = "设置"

    name=models.CharField(max_length=80)        
    value=models.CharField(max_length=2000)    
   

class Page(UBaseModel):
    class Meta:
        db_table="uublog_page"
        verbose_name = "页面管理"
        verbose_name_plural = "页面管理"

    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
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
    cancomment=models.BooleanField(default=True)       
    password=models.CharField(max_length=80)       















