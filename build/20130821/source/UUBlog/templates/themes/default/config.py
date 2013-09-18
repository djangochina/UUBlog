#-*- coding:utf-8 -*-
import sys 
import datetime
import os
import importlib

config={}
config.setdefault("theme","default")
config.setdefault("name","name")
config.setdefault("description","description")

#首页可用的模板
config.setdefault("indextemplate",{"normal","默认"})

#列表页可用的模板
config.setdefault("listtemplate",{"normal":"默认","cat":"分类列表","tag":"Tag列表"})

#文章页面可用的模板
config.setdefault("posttemplate",{"normal":"默认","link":"连接模板","image":"图片"})

#单独页面可用的模板
config.setdefault("pagetemplate",{"normal":"默认"})

#单独页面可用的模板
config.setdefault("searchtemplate",{"normal":"默认"})





