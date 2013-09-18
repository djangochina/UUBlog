#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from UUBlog.common import pub,utility,filehelper
from UUBlog.models import Attachment
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

        self.SetTemplateName("attachlist")
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('okFilter'):
            catId=self.GetPostData("catTree")
            status=self.GetPostData("status")
            istop=self.GetPostData("istop")
            time=self.GetPostData("time")
            keywords=self.GetPostData("keywords")

            queryString="catid=%s&status=%s&istop=%s&time=%s&keywords=%s" %(catId,status,istop,time,keywords)
            self.redirectUrl="/admin/attachlist/?"+queryString
            
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
            self.redirectUrl="/admin/attachmentlist/"
        else:
            self.SetTemplateName("attach")
           
        return locals()

    def PostContext(self, **kwargs):
      
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

        self.post_context_data(**kwargs)
        #context = self.post_context_data(**kwargs)
     
        return HttpResponse("1", mimetype="text/plain")

    def GetContext(self, **kwargs):
        return HttpResponse("0", mimetype="text/plain")

        self.SetTemplateName("attachlist")
        return locals()

    def PostContext(self, **kwargs):
        for field_name in self.request.FILES:
            
            uploaded_file = self.request.FILES[field_name]
            self.SaveFile(uploaded_file)

        return locals()            


    
    
    
    
    
    
    
    
    

