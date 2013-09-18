#-*- coding:utf-8 -*-
#http://leatherbound-blue.4templat.es/
import sys 
import datetime
import os
import importlib

config={}
config.setdefault("theme","leatherbound-blue")
config.setdefault("name","追忆")
config.setdefault("description","description")
config.setdefault("basepagepath","themes/%s/basepage.html" %config["theme"])
config.setdefault("containerpath","themes/%s/container.html" %config["theme"])

#首页可用的模板
config.setdefault("indextemplate",{"normal":"默认","image":"图片"})

#分类
config.setdefault("cattemplate",{"normal":"默认"})

#Tag
config.setdefault("tagtemplate",{"normal":"默认"})

#搜索
config.setdefault("searchtemplate",{"normal":"默认"})

#文章可用的模板
config.setdefault("posttemplate",{"normal":"默认","link":"连接","image":"图片"})

#单页面可用的模板
config.setdefault("pagetemplate",{"normal":"默认"})





