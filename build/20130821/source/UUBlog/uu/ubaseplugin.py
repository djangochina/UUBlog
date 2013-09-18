#-*- coding:utf-8 -*-

from UUBlog.init import *

#hookList={}

#hookList.setdefault("plugin_Activate ",[])           #显示之前
#hookList.setdefault("plugin_Deactivate",[])           #显示之前
#hookList.setdefault("post_BeforShow",[])           #显示之前
#hookList.setdefault("post_BeforAdd",[])        #发布之前
#hookList.setdefault("post_AfterAdd",[])        #发布之前
#hookList.setdefault("post_BeforDelete",[])        #发布之前
#hookList.setdefault("post_AfterDelete",[])        #发布之前

class UBasePlugin(object):


   pass




def AddHook(key,func):
    global G

    if not G["hooks"].has_key(key):
        G["hooks"].setdefault(key,[])
    G["hooks"][key].append(func)

def RemoveHook(key,func):
    global G

    if G["hooks"].has_key(key):
        G["hooks"][key].remove(func)
    









