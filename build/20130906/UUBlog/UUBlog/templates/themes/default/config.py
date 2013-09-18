#-*- coding:utf-8 -*-
import sys 
import datetime
import os
import importlib

config={}
config.setdefault("theme","default")
config.setdefault("name","默认")
config.setdefault("description","description")

#首页可用的模板
config.setdefault("indextemplate",{"normal":"默认"})

config.setdefault("cattemplate",{"normal":"默认"})

config.setdefault("tagtemplate",{"normal":"默认"})

config.setdefault("searchtemplate",{"normal":"默认"})

#文章页面可用的模板
config.setdefault("posttemplate",{"normal":"默认","link":"连接","image":"图片"})

#单独页面可用的模板
config.setdefault("pagetemplate",{"normal":"默认"})





