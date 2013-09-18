#-*- coding:utf-8 -*-

from django import template
from UUBlog.common import utility

register=template.Library()



def DoTitlePic(value):
    if value is None or value=="":
        pass
    dataFrom=value[0:4]
    if dataFrom=="http":
        return value
    elif value.find("/media/")>-1:
        return value

    return "/media/"+value

register.filter("DoTitlePic",DoTitlePic)


def DoRender(context, html,contextData,key="key"):
    from django.template import Template
    from django.template import Context;
    tpl = Template(html)
    return tpl.render(Context({"widget":context}))

register.simple_tag(takes_context=True)(DoRender)


def DoDateTime(context,datetimeValue,options):
    ret=datetime.datetime.now()

    if datetimeValue=="" or datetimeValue is None:
        datetimeValue=datetime.datetime.now()

    datetimeformat=utility.GetDicData(options,"datetimeformat",None)
    if datetimeformat is not None:
        ret=""
   
  

    return ret

register.simple_tag(takes_context=True)(DoDateTime)

#自定义头部样式和背景样式
def DoCustomStyle(context, options):

    style="""<style type="text/css">"""

    #头部高度
    headerstyle_height=utility.ToInt(utility.GetDicData(options,"headerstyle_height"),0)
    if headerstyle_height>0:
        style+="""#header {height: %spx;}""" % headerstyle_height

    headerstyle_status=utility.GetDicData(options,"headerstyle_status","none")
    backgroundstyle_status=utility.GetDicData(options,"backgroundstyle_status","none")

    if headerstyle_status=="none" and backgroundstyle_status=="none":
        pass
    else:
        #头部样式
        headerstyle_color=utility.GetDicData(options,"headerstyle_color","none")
        headerstyle_image=utility.GetDicData(options,"headerstyle_image","none")
        headerstyle_repeat=utility.GetDicData(options,"headerstyle_repeat","none")
        headerstyle_horizontal=utility.GetDicData(options,"headerstyle_horizontal","none")
        headerstyle_vertical=utility.GetDicData(options,"headerstyle_vertical","none")
    
        if headerstyle_status=="both":
            style+="""#header {background: %s url(/media%s) %s %s %s;}""" %(headerstyle_color,headerstyle_image,headerstyle_repeat,headerstyle_horizontal,headerstyle_vertical)
        elif headerstyle_status=="image":
            style+="""#header {background: %s url(/media%s) %s %s %s;}""" %("transparent",headerstyle_image,headerstyle_repeat,headerstyle_horizontal,headerstyle_vertical)
        elif headerstyle_status=="color":
            style+="""#header {background: %s;}""" %(headerstyle_color)

    

        #背景样式
        backgroundstyle_color=utility.GetDicData(options,"backgroundstyle_color","none")
        backgroundstyle_image=utility.GetDicData(options,"backgroundstyle_image","none")
        backgroundstyle_repeat=utility.GetDicData(options,"backgroundstyle_repeat","none")
        backgroundstyle_horizontal=utility.GetDicData(options,"backgroundstyle_horizontal","none")
        backgroundstyle_vertical=utility.GetDicData(options,"backgroundstyle_vertical","none")
    
        if backgroundstyle_status=="both":
            style+="""body {background: %s url(/media%s) %s %s %s;}""" %(backgroundstyle_color,backgroundstyle_image,backgroundstyle_repeat,backgroundstyle_horizontal,backgroundstyle_vertical)
        elif backgroundstyle_status=="image":
            style+="""body {background: %s url(/media%s) %s %s %s;}""" %("transparent",backgroundstyle_image,backgroundstyle_repeat,backgroundstyle_horizontal,backgroundstyle_vertical)
        elif backgroundstyle_status=="color":
            style+="""body {background: %s;}""" %(backgroundstyle_color)
   


    style+="""</style>"""

    return style

register.simple_tag(takes_context=True)(DoCustomStyle)


#对url中的查询字符串操作
def DoQueryString(context, currentQueryString,**appendQueryString):
    
    queryStringDic={}
    queryStringArray=currentQueryString.split("&")

    for queryStringItem in queryStringArray:
        itemArray=queryStringItem.split("=")
        if len(itemArray)==2:
            queryStringDic.setdefault(itemArray[0],itemArray[1])

    for key,value in appendQueryString.items():
        if queryStringDic.has_key(key):
            if value is None or value=="":
                del queryStringDic[key]
            else:
                queryStringDic[key]=value
        else:
            queryStringDic.setdefault(key,value)

    retQueryString=""
    for key,value in queryStringDic.items():
        retQueryString+="%s=%s&" %(key,value)
        
    return retQueryString.rstrip("&")

register.simple_tag(takes_context=True)(DoQueryString)






