#-*- coding:utf-8 -*-

import time,datetime
import os
import re


def RemoveTags(str_html):
    return re.compile('</?\w+[^>]*>').sub('',str_html)




def Json2Obj(str,default={}):
    
    try:
        import json
        return json.loads(str)
    except:
        return default
def Obj2Json(obj,default=''):
    
    try:
        import json
        return json.dumps(obj)
    except:
        return default


def GetImgSrc(html):
    pattern="""\w*<img.+?src=(?:'|\")(?P<src>.+?)(?:'|\").*?(?:\/).*?>\w*"""
    import re
    result=re.findall(pattern,html)
    return result
   












