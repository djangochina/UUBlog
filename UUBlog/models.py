#-*- coding:utf-8 -*-

import datetime
from django.contrib.auth.models import User

from UUBlog.settings import TablePrefix
from UUBlog.core.ubasemodel import *


class Category(UBaseModel):
    class Meta:
        db_table=TablePrefix+"category"
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
    sidebarfloat=models.CharField(max_length=80)

class Post(UBaseModel):
    class Meta:
        db_table=TablePrefix+"post"
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
    lastcommenttime=models.DateTimeField(default=datetime.datetime.now())
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
    sidebarfloat=models.CharField(max_length=80)

class Page(UBaseModel):
    class Meta:
        db_table=TablePrefix+"page"
        verbose_name = "页面管理"
        verbose_name_plural = "页面管理"

    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    createtime=models.DateTimeField(default=datetime.datetime.now())
    lastcommenttime=models.DateTimeField(default=datetime.datetime.now())
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
    sidebarfloat=models.CharField(max_length=80)

class Comment(UBaseModel):
    class Meta:
        db_table=TablePrefix+"comment"
        verbose_name = "评论管理"
        verbose_name_plural = "评论管理"
    obj_id=models.IntegerField(default=0)
    obj_type=models.CharField(max_length=80) #post,page
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
        db_table=TablePrefix+"attachment"
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
        db_table=TablePrefix+"sidebar"
        verbose_name = "侧边框"
        verbose_name_plural = "侧边框"
    id=models.CharField(max_length=80,primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

class MyWidget(UBaseModel):
    class Meta:
        db_table=TablePrefix+"mywidget"
        verbose_name = "我的Widget管理"
        verbose_name_plural = "我的Widget管理"
    #def __unicode__(self):
    #    return self.title
    sidebar_id=models.CharField(max_length=80)
    widget=models.CharField(max_length=80)
    title=models.CharField(max_length=80)
    isshowtitle=models.BooleanField(default=False)     
    params=models.CharField(max_length=2000)   
    data=models.CharField(max_length=2000)       
    sortnum=models.IntegerField(default=0)

class Navigate(UBaseModel):
    class Meta:
        db_table=TablePrefix+"navigate"
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
        db_table=TablePrefix+"option"
        verbose_name = "设置"
        verbose_name_plural = "设置"

    name=models.CharField(max_length=80)        
    value=models.CharField(max_length=2000)    
   


   
class UserProfile(UBaseModel):
    class Meta:
        app_label="userprofile"
        db_table=TablePrefix+"userprofile"
        
    user=models.ForeignKey(User,unique=True)
    #头像
    avatar=models.ImageField(upload_to='avatar')

    #基本信息
    nickname=models.CharField(max_length=80)
    realname=models.CharField(max_length=80)
    gender=models.IntegerField(default=0)
    birthday=models.DateTimeField(default=datetime.datetime.now())
    birthcity=models.CharField(max_length=80)
    residecity=models.CharField(max_length=80)

    #个人信息
    affectivestatus=models.IntegerField(default=0)
    lookingfor=models.IntegerField(default=0)
    bloodtype=models.IntegerField(default=0)
    site=models.CharField(max_length=80)
    bio=models.CharField(max_length=255)
    interest=models.CharField(max_length=255)
    sightml=models.CharField(max_length=255)
    timeoffset=models.CharField(max_length=80)
   
    #联系方式
    qq=models.CharField(max_length=80)
    msn=models.CharField(max_length=80)
    taobao=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    phone=models.CharField(max_length=80)
    mobile=models.CharField(max_length=80)
    address=models.CharField(max_length=80)
    zipcode=models.CharField(max_length=80)











