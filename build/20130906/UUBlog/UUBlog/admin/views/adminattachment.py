#-*- coding:utf-8 -*-
import uuid
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import time,datetime
from django.db.models import Q
from django.db import connection
from django.template import RequestContext 
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.common import pub,utility,filehelper

from UUBlog.models import *
from UUBlog.uu.ubaseblog import *

from UUBlog.uu.ubaseadmin import UBaseAdminView

#分类浏览
class AttachmentManagerView(UBaseAdminView):

    def GetContext(self, **kwargs):
        filetype=utility.ToInt(self.GetGetData("filetype"),None)

        attachList=Attachment.objects.all().order_by("-createtime")
        if filetype:
            attachList=attachList.filter(filetype=filetype)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("admin_pagesize",10)

        attachList=pub.GetPagedObject(attachList,pageIndex,pageSize)
        pageObject=attachList

        self.template_name="admin/attachlist.html"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('okFilter'):
            catId=self.GetPostData("catTree")
            status=self.GetPostData("status")
            istop=self.GetPostData("istop")
            time=self.GetPostData("time")
            keywords=self.GetPostData("keywords")

            queryString="catid=%s&status=%s&istop=%s&time=%s&keywords=%s" %(catId,status,istop,time,keywords)
            self.returnUrl="/admin/attachlist/?"+queryString
            
        return locals()

#文章页面
class AttachmentEditView(UBaseAdminView):

    def GetContext(self, **kwargs):
        action=self.GetGetData("action","edit")
        if action=="delete":
            aid=utility.ToInt(utility.GetDicData(kwargs,"aid"),0)
            attachInfo=Attachment.objects.get(id=aid)
            attachInfo.delete()

            from UUBlog import settings
            filehelper.DeleteFile(settings.MEDIA_ROOT+attachInfo.path)

            self.currentQueryString=self.BuildQueryString(self.currentQueryDic,action=None)
            self.returnUrl="/admin/attachmentlist/"
        else:
            self.template_name="admin/attach.html"
           
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):

            pid=int(kwargs.get("pid",0))

            try:
                postInfo=Post.objects.get(id=pid)
              
            except:
                postInfo=Post()

            category=Category.objects.get(id=self.GetPostData('catTree'))

            postInfo.category=category
            
            SetPostValues(self.request,postInfo)

            titlepic=None
            if self.request.FILES.has_key("titlepic"):
                titlepic = self.request.FILES['titlepic']

                #20130711205603+guid
                #201307/11/205603+guid
                currentTime=datetime.datetime.now()
                path="%s/%s/%s/" %("blog/attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
                filename="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())
                
                savedInfo=pub.SaveFile(titlepic,path,filename)
                postInfo.titlepic=savedInfo[0]

            else:
                pics=utility.GetImgSrc(postInfo.content)
                if pics:
                    postInfo.titlepic=pics[0]
                        
            postInfo.save()

            

            if titlepic:
                attachmentInfo=Attachment()
                attachmentInfo.article_id=postInfo.id
                attachmentInfo.user_id=self.currentUser.id
                attachmentInfo.filepath=savedInfo[0]
                attachmentInfo.filename=savedInfo[1]
                attachmentInfo.filetitle=savedInfo[2]
                attachmentInfo.extension=savedInfo[3]
                attachmentInfo.createtime=datetime.datetime.now()

                attachmentInfo.save()

            #更新分类统计信息 不是默认分类并且是发布的文章
            if category.id !=1 and postInfo.status:
                category.posts+=1
                category.save()

        self.template_name="blog/pub/articleedit.html"

        return locals()



@csrf_exempt
def UploadFileHandler(request):
    if request.method == 'POST':
        for field_name in request.FILES:
            uploaded_file = request.FILES[field_name]
            pub.SaveFile(uploaded_file,"\\attachment")
          

        # indicate that everything is OK for SWFUpload
        return HttpResponse("1", mimetype="text/plain")

    else:
        # show the upload UI
        return HttpResponse("0", mimetype="text/plain")

class AttachmentUploadView(UBaseAdminView):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AttachmentUploadView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        context = self.post_context_data(**kwargs)
     
        return HttpResponse("1", mimetype="text/plain")

    def GetContext(self, **kwargs):
        return HttpResponse("0", mimetype="text/plain")

        self.template_name="admin/attachlist.html"

        return locals()

    def PostContext(self, **kwargs):
        for field_name in self.request.FILES:
            #20130711205603+guid
            #201307/11/205603+guid
            currentTime=datetime.datetime.now()
            path="\\%s\\%s\\%s" %("attachment",currentTime.strftime("%Y%m"),currentTime.strftime("%d"))
            fileName="%s%s" %(currentTime.strftime("%H%M%S"),uuid.uuid1())

            uploaded_file = self.request.FILES[field_name]
            uploadFileInfo=pub.SaveFile(uploaded_file,path,fileName)
            attachInfo=Attachment()
            attachInfo.path=uploadFileInfo["path"]
            attachInfo.name=uploadFileInfo["newname"]
            attachInfo.title=uploadFileInfo["name"]
            attachInfo.description=uploadFileInfo["name"]
            attachInfo.extension=uploadFileInfo["ext"]

            filetype=10
            if attachInfo.extension in self.options["filetype_image"]:
                filetype=1
            elif attachInfo.extension in self.options["filetype_media"]:
                filetype=2
            elif attachInfo.extension in self.options["filetype_file"]:
                filetype=3

            attachInfo.filetype=filetype
            attachInfo.createtime=datetime.datetime.now()

            attachInfo.save()

        return locals()            


    
    
    
    
    
    
    
    
    
               