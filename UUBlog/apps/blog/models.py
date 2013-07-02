#-*- coding:utf-8 -*-
import datetime
from UUBlog.core.ubasemodel import *
from django.utils import timezone
from django.contrib.auth.models import User

class Category(UBaseModel):
    class Meta:
        db_table="blog_category"
    name=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)

class Article(UBaseModel):
    class Meta:
        db_table="blog_article"
    channel1_id=models.IntegerField(default=0)
    channel2_id=models.IntegerField(default=0)
    category=models.ForeignKey(Category)
    title=models.CharField(max_length=200)
    pic=models.CharField(max_length=80)
    tags=models.CharField(max_length=120)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    createtime=models.DateTimeField(default="0000-00-00 00:00:00")
    views=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    goods=models.IntegerField(default=0)
    bads=models.IntegerField(default=0)
    status=models.IntegerField(default=1)       #1发布；0草稿
    user_id=models.IntegerField(default=1)
    username=models.CharField(max_length=80)
    ishome=models.IntegerField(default=0)       #1发布；0草稿
    isrecommend=models.IntegerField(default=0)       #1发布；0草稿
    istop=models.IntegerField(default=0)       #1发布；0草稿
    isoriginal=models.IntegerField(default=1)       #1发布；0草稿
    cancomment=models.IntegerField(default=1)       #1发布；0草稿
    password=models.CharField(max_length=80)       #1发布；0草稿



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
    todayviews=models.IntegerField(default=0)
    totalviews=models.IntegerField(default=0)
    articles=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    suggestes=models.IntegerField(default=0)
    lastsuggesttime=models.DateTimeField(default=datetime.datetime.now())
    createtime=models.DateTimeField(default=datetime.datetime.now())

class Channel(UBaseModel):
    class Meta:
        db_table="blog_channel"
    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    users=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=80)
    isenable=models.IntegerField(default=1)

class Type(UBaseModel):
    class Meta:
        db_table="blog_type"
    parent_id=models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    sortnum=models.IntegerField(default=10)
    articles=models.IntegerField(default=0)
    users=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=80)
    isenable=models.IntegerField(default=1)

class BlogType(UBaseModel):
    class Meta:
        db_table="blog_blogtype"
    blog_id=models.IntegerField(default=0)
    type_id=models.IntegerField(default=0)
    isrecommend=models.IntegerField(default=1)
 
class Follow(UBaseModel):
    class Meta:
        db_table="blog_follow"
    blog_id=models.IntegerField(default=0)
    follow_blog_id=models.IntegerField(default=0)


class Suggest(UBaseModel):
    class Meta:
        db_table="blog_suggest"
    blog_id=models.IntegerField(default=0)
    suggest_blog_id=models.IntegerField(default=0)


class Visit(UBaseModel):
    class Meta:
        db_table="blog_visit"
    blog_id=models.IntegerField(default=0)
    visit_blog_id=models.IntegerField(default=0)
    lastvisittime=models.DateTimeField(default=datetime.datetime.now())