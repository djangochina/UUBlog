#-*- coding:utf-8 -*-
import datetime
from UUBlog.core.ubasemodel import *
from django.utils import timezone
from django.contrib.auth.models import User



    
  
class UserProfile(UBaseModel):
    class Meta:
        #app_label="accounts"
        db_table="accounts_userprofile"
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


