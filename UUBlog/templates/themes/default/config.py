#-*- coding:utf-8 -*-
import sys 
import datetime
import os
import importlib

config = {}
config.setdefault("theme", "default")
config.setdefault("name", "默认")
config.setdefault("description", "description")
config.setdefault("basepagepath", "themes/%s/basepage.html" % config["theme"])
config.setdefault("containerpath", "themes/%s/container.html" % config["theme"])

#首页可用的模板
config.setdefault("indextemplate", {"default": "默认", "image": "图片"})

#分类
config.setdefault("cattemplate", {"default": "默认"})

#Tag
config.setdefault("tagtemplate", {"default": "默认"})


#文章可用的模板
config.setdefault("posttemplate", {"default": "默认", "link": "连接", "image": "图片"})

#单页面可用的模板
config.setdefault("pagetemplate", {"default": "默认"})





