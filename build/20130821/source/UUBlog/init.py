#-*- coding:utf-8 -*-
import sys 
import datetime
import os
import importlib


G={}
G.setdefault("plugins",{})
G.setdefault("hooks",{})#{"addpost":[func1,func2,func3],}

def GetSysTime():
    return datetime.datetime.now()



def LoadWidgets():
    ret={}
  
    dirs=os.listdir("UUBlog/widgets")
    for dir in dirs:
        if dir.find(".")>0:
            continue
        moduleName="%s.%s.%s.%s" %("UUBlog","widgets",dir,dir)
        module=importlib.import_module(moduleName)
        ret.setdefault(dir,module)
    return ret

G.setdefault("widgets",LoadWidgets())


def LoadPlugins():
    ret={}

    dirs=os.listdir("UUBlog/plugins")
    for dir in dirs:
        if dir.find(".")>0:
            continue
        moduleName="%s.%s.%s.%s" %("UUBlog","plugins",dir,dir)
        module=importlib.import_module(moduleName)
        ret.setdefault(dir,module)
    return ret

G.setdefault("plugins",LoadPlugins())















