#-*- coding:utf-8 -*-
import os
from UUBlog import settings

#cookie

def SetCookie(response,key,value):
    response.set_cookie(key,value)
    
def GetCookie(request,key,defaultValue=None):
    if request.COOKIES.has_key(key):
        return request.COOKIES[key]
    return defaultValue
def DelCookie(response,key):
    response.delete_cookie(key,path="/")

#session
def HasSession(request,key):
    return key in request.session

def SetSession(request,key,value):
    request.session[key]=value

def GetSession(request,key,defaultValue=None,isDelete=False):
    
    if HasSession(request,key):
        ret= request.session[key]
        if isDelete:
            DelSession(request,key)
        return ret

    return defaultValue

def DelSession(request,key):
    if HasSession(request,key):
        del request.session[key]

def HasPostData(request,key):
    if request:
        return request.POST.has_key(key)
    return False

def GetPostData(request,key,defaultValue=""):
    ret=""
    if HasPostData(request,key):
        ret= request.POST[key]
    if ret is None or ret=="":
        ret=defaultValue
    return ret

def HasGetData(request,key):
    if request:
        return request.GET.has_key(key)
    return False

def GetGetData(request,key,defaultValue=""):
    ret=""
    if HasGetData(request,key):
        ret= request.GET[key]
    if ret is None or ret=="":
        ret= defaultValue

    return ret

def HasFile(request,key):
    if request:
        return request.FILES.has_key(key)
    return False

def GetFile(request,key):
    if HasFile(request,key):
        ret=request.FILES[key]
        return ret;
    return None
   

def GetRequestListData(request,key,default=""):
    if request:
        return request.REQUEST.getlist(key)
    return default



def GetFileExtension(fileName):
    if fileName is None or fileName=="":
        return ""

    dot=fileName.rfind(".")
    if dot>-1:
        return fileName[dot:]
    else:
        return ""


#path："aaa/bbb/ccc/
#fileName:"xxx"（不带扩展名）
def SaveFile(uploadFile,path,fileNewName=None):
    rootPath=settings.MEDIA_ROOT+path+"\\"
    rootPath=rootPath.replace("/","\\")
    if not os.path.isdir(rootPath):
        os.makedirs(rootPath)

    fileName=uploadFile._get_name()
    dot=fileName.rfind(".")
    fileInfo=[]
    if dot>-1:
        fileInfo.append(fileName[0:dot])
        fileInfo.append(fileName[dot:])
    else:
        fileInfo.append(fileName)
        fileInfo.append("")

    if fileNewName is None or fileNewName=="":
        fileNewName=fileInfo[0]
    fileFullPath=rootPath+fileNewName+fileInfo[1]
    fd=open(fileFullPath,'wb')
    for chunk in uploadFile.chunks():
        fd.write(chunk)
    fd.close()

    
    fileUrlPath=(path+"\\").replace("\\","/")+fileNewName+fileInfo[1]

    ret={}

    #文件路径
    ret.setdefault("path",fileUrlPath)
    #新文件名字
    ret.setdefault("newname",fileNewName+fileInfo[1])
    #原有文件名字
    ret.setdefault("name",fileInfo[0])
    ret.setdefault("ext",fileInfo[1])#文件扩展名

   
    return ret


def ExecuteSql(sql,isQuery=True):
    if sql is None or sql=="":
        return 

    from django.db import connection
    cursor = connection.cursor()

    cursor.execute(sql)
    if isQuery:
        fetchall = cursor.fetchall()
        return fetchall
    else:
        connection.commit()
    cursor.close() 


def GetPagedObject(objectList,currentIndex,pageSize):
    if pageSize is None or pageSize=="":
        pageSize=20

    from django.core.paginator import Paginator
    p=Paginator(objectList,int(pageSize))

    if currentIndex<1:
        currentIndex=1

    if currentIndex>p.num_pages:
        currentIndex=p.num_pages

    result=p.page(currentIndex)

    return result















