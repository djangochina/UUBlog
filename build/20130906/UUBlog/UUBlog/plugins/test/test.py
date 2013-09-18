#-*- coding:utf-8 -*-

from UUBlog.core.ubaseplugin import *

class Test(UBasePlugin):
    def __init__(self, **kwargs):
       super(Test, self).__init__(**kwargs)
       self.aaaa=0
       self.AddHook("post_BeforShow",self.AddTest)
      
    def aaa(self):
        pass
    def AddTest(self,postInfo):
        postInfo.content="xxxxxxxxxxxxx"+postInfo.content
        return postInfo

def AddTest(postInfo):
        postInfo.content="xxxxxxxaaaaaaaaaaaaaaxxxxxx"+postInfo.content
        return postInfo
AddHook("post_BeforShow",AddTest)     