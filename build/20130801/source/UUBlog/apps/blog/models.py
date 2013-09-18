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
        db_table="blog_category"
    def __unicode__(self):
        return self.name

    name=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    isnav=models.BooleanField(default=False)
    user_id=models.IntegerField(default=0)
    
class Article(UBaseModel):
    class Meta:
        db_table="blog_article"
    channel1_id=models.IntegerField(default=0)
    channel2_id=models.IntegerField(default=0)
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
        db_table="blog_comment"
    article=models.ForeignKey(Article)
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=80)
    content=models.TextField()
    createtime=models.DateTimeField(default="0000-00-00 00:00:00")
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    reply_id=models.IntegerField(default=0)
    

class Blog(UBaseModel):
    class Meta:
        db_table="blog_blog"
    def __unicode__(self):
        return self.title

    id=models.IntegerField(default=0,primary_key=True)
    avatar=models.CharField(max_length=80)
    domain=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    keywords=models.CharField(max_length=200)
    about=models.CharField(max_length=500)
    announcement=models.CharField(max_length=500)
    types=models.CharField(max_length=200)
    listenchannels=models.CharField(max_length=200)
    modules=models.CharField(max_length=1000)
    template=models.CharField(max_length=50)
    css=models.CharField(max_length=500)
    headhtml=models.CharField(max_length=500)
    footerhtml=models.CharField(max_length=500)
    follows=models.IntegerField(default=0)
    befollows=models.IntegerField(default=0)
    todayviews=models.IntegerField(default=0)
    totalviews=models.IntegerField(default=0)
    articles=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    suggestes=models.IntegerField(default=0)
    lastsuggesttime=models.DateTimeField(default=datetime.datetime.now())
    createtime=models.DateTimeField(default=datetime.datetime.now())

#文章频道
class Channel(UBaseModel):
    class Meta:
        db_table="blog_channel"
    def __unicode__(self):
        return self.name

    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    namecn=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    isenable=models.BooleanField(default=True)

#博客类型
class Type(UBaseModel):
    class Meta:
        db_table="blog_type"
    def __unicode__(self):
        return self.name

    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    namecn=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    blogs=models.IntegerField(default=0)
    isenable=models.BooleanField(default=True)

class BlogType(UBaseModel):
    class Meta:
        db_table="blog_blogtype"
    blog_id=models.IntegerField(default=0)
    type_id=models.IntegerField(default=0)
 
#博客关注
class Follow(UBaseModel):
    class Meta:
        db_table="blog_follow"
    blog_id=models.IntegerField(default=0)
    follow_blog_id=models.IntegerField(default=0)

#博客推荐
class Suggest(UBaseModel):
    class Meta:
        db_table="blog_suggest"
    blog_id=models.IntegerField(default=0)
    suggest_blog_id=models.IntegerField(default=0)

#博客访客记录
class Visit(UBaseModel):
    class Meta:
        db_table="blog_visit"
    blog_id=models.IntegerField(default=0)
    visit_blog_id=models.IntegerField(default=0)
    lastvisittime=models.DateTimeField(default=datetime.datetime.now())


class Attachment(UBaseModel):
    class Meta:
        db_table="blog_attachment"
    article_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    filepath=models.CharField(max_length=80)        #blog/attachment/201307/11/163608jc01h66y6cjbc6cf.jpg，年月/日/时分秒32位guid
    filename=models.CharField(max_length=80)    #163608jc01h66y6cjbc6cf.jpg
    filetitle=models.CharField(max_length=80)    #原有的文件名
    extension=models.CharField(max_length=10)   #jpg
    createtime=models.DateTimeField(default=datetime.datetime.now())

class BlockCategory(UBaseModel):
    class Meta:
        db_table="blog_block_category"
        verbose_name = "碎片分类"
        verbose_name_plural = "碎片分类"

    def __unicode__(self):
        return '%s' %(self.namecn) 
   
    namecn=models.CharField(max_length=80)
  

class Block(UBaseModel):
    class Meta:
        db_table="blog_block"
        verbose_name = "碎片管理"
        verbose_name_plural = "碎片管理"
    def __unicode__(self):
        return '%s(%s,%s)' %(self.namecn,"代码碎片" if self.type==1 else "静态碎片",self.name) 
    TYPE_CHOICES = (
        (1, "代码碎片"),
        (2, "静态碎片"),
    )
    blockcategory=models.ForeignKey(BlockCategory,db_column="block_category_id")
    name=models.CharField(max_length=80)
    namecn=models.CharField(max_length=80,verbose_name='碎片名称')
    type=models.IntegerField(default=1,choices=TYPE_CHOICES)         #1—代码碎片；2—静态碎片（可直接录入，也可推送文章生成）；
    createtime=models.DateTimeField(default=datetime.datetime.now())

#1—代码碎片
class Block1(UBaseModel):
    class Meta:
        db_table="blog_block_1"
        verbose_name = "代码碎片管理"
        verbose_name_plural = "代码碎片管理"
    block=models.ForeignKey(Block)
    content=models.TextField()
    createtime=models.DateTimeField(default=datetime.datetime.now())


#2—静态碎片
class Block2(UBaseModel):
    class Meta:
        db_table="blog_block_2"
        verbose_name = "静态碎片管理"
        verbose_name_plural = "静态碎片管理"

    block=models.ForeignKey(Block) 
    title=models.CharField(max_length=200)
    titlestyle=models.CharField(max_length=80)
    titlepic=models.CharField(max_length=80)
    titleurl=models.CharField(max_length=80)
    summary=models.CharField(max_length=500)
    createtime=models.DateTimeField(default=datetime.datetime.now())



#证券理财
#理财技巧
#产经发展
#经济管理


#INSERT INTO  `uublog`.`blog_channel`(parent_id,name) values(22,'证券理财');
#INSERT INTO  `uublog`.`blog_channel`(parent_id,name) values(22,'理财技巧');
#INSERT INTO  `uublog`.`blog_channel`(parent_id,name) values(22,'产经发展');
#INSERT INTO  `uublog`.`blog_channel`(parent_id,name) values(22,'经济管理');
#INSERT INTO  `uublog`.`blog_channel`(parent_id,name) values(18,'美容瘦身');



class Widget(UBaseModel):
    class Meta:
        db_table="blog_widget"
        verbose_name = "Widget管理"
        verbose_name_plural = "Widget管理"

    DATAFROM_CHOICES = (
        ("func", "函数调用"),
        ("sql", "sql调用"),
        ("block", "碎片调用"),
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
    block=models.CharField(max_length=256,null=True,blank=True)          #碎片名称
    defaultdata=models.CharField(max_length=256,null=True,blank=True)    #默认数据
    jsondef=models.CharField(max_length=2000,null=True,blank=True)       #datafrom为json时，定义json的对象
    canedit=models.BooleanField(default=False)          #是否可编辑默认数据
    render=models.CharField(max_length=2000)        #render模板代码
    issys=models.BooleanField(default=False)            #是否是系统widget
    sortnum=models.IntegerField(default=0)          #显示顺序

class BlogWidget(UBaseModel):
    class Meta:
        db_table="blog_blog_widget"
    blog_id=models.IntegerField(default=0)
    widget=models.ForeignKey(Widget)
    title=models.CharField(max_length=80)  
    params=models.CharField(max_length=2000)   
    attvalues=models.CharField(max_length=2000)
    datavalues=models.CharField(max_length=2000)       
    sortnum=models.IntegerField(default=0)








