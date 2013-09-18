#-*- coding:utf-8 -*-



def RemoveTags(str_html):
    import re
    return re.compile('</?\w+[^>]*>').sub('',str_html)




def Json2Obj(inputStr,default={}):
    
    try:
        import json
        return json.loads(inputStr)
    except:
        return default
def Obj2Json(obj,default=''):
    
    try:
        import json
        return json.dumps(obj)
    except:
        return default

def HasDicData(dic,key):
    if dic:
        return dic.has_key(key)
    return False

def GetDicData(dic,key,default=''):
    if HasDicData(dic,key):
        return dic[key]
    return default


def GetImgSrc(html):
    pattern="""\w*<img.+?src=(?:'|\")(?P<src>.+?)(?:'|\").*?(?:\/).*?>\w*"""
    import re
    result=re.findall(pattern,html)
    return result
   

def ToInt(s,defaultValue=0):
    if s is None or s=="":
        return defaultValue
    try:
        ret=int(s)
    except:
        ret=defaultValue
    return ret












