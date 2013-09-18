#-*- coding:utf-8 -*-
import re
import datetime

from django import template
from UUBlog.common import utility

register=template.Library()



def DoTitlePic(value):
    if value is None or value=="":
        return "/media/default.png"

    dataFrom=value[0:4]
    if dataFrom=="http":
        return value
    elif value.find("/media/")>-1:
        return value

    return "/media/"+value

register.filter("DoTitlePic",DoTitlePic)

def DoTemplateExists(parser, token):
   

    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    template_name, var_name = m.groups()
    
    return TemplateExistsNode(template_name, var_name)

   

class TemplateExistsNode(template.Node):
    def __init__(self, template_name,var_name):
        self.isString=False
        if template_name[0] == template_name[-1] and template_name[0] in ('"', "'"):
            self.template_name=template_name[1:-1]
            self.isString=True
        else:
            self.template_name = template.Variable(template_name)
        
        self.var_name = var_name
    def render(self, context):
        try:
            if self.isString:
                template.loader.get_template(self.template_name)
            else:
                actual_template_name = self.template_name.resolve(context)
                template.loader.get_template(actual_template_name)
            context[self.var_name]=True
        except template.TemplateDoesNotExist:
            context[self.var_name]=False

        return ''
register.tag('DoTemplateExists', DoTemplateExists)


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






