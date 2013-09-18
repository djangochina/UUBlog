from UUBlog.apps.blog.models import *
from django import template
register=template.Library()


def GetBlockValue(value,name):
    from UUBlog.apps.blog.views import viewblock
    datas=viewblock.GetBlockValue(name)

    return datas
   
register.filter("GetBlockValue",GetBlockValue)


def Render(value,context):
    from django.template import Template
    from django.template import Context;
    tpl = Template(value)
    return tpl.render(Context({"widget":context}))


register.filter("Render",Render)

def TitlePic(value):
    if value is None or value=="":
        pass
    dataFrom=value[0:4]
    if dataFrom=="http":
        return value
    elif value.find("/media/")>-1:
        return value

    return "/media/"+value


register.filter("TitlePic",TitlePic)