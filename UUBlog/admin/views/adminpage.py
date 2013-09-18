#-*- coding:utf-8 -*-

import datetime

from UUBlog.common import pub,utility
from UUBlog.models import Page
from UUBlog.uu.ubaseadmin import UBaseAdminView



#page manage
class PageListView(UBaseAdminView):

    def GetContext(self, **kwargs):
       
        status= utility.ToInt(utility.GetDicData(kwargs,"status"),-1)

        pageList=self.GetPageList()
      
        if status>-1:
            pageList=pageList.filter(status=status)

        self.SetTemplateName("pagelist")
        return locals()



#edit or create new page
class PageEditView(UBaseAdminView):

    def GetContext(self, **kwargs):
       
        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)
        action=self.GetGetData("action","edit")

        if action=="edit":
            if pid>0:
                pageInfo=self.GetPage(pid)
                if pageInfo is None:
                    self.message="页面不存在"
                    self.SetTemplateName("message")
                    self.redirectUrl="/admin/pagelist/"
                    self.autoRedirect=False
                    return locals()
            else:
                pageInfo=Page()
           
            self.SetTemplateName("page")

        else:
            if action=="delete":
                Page.objects.filter(id=pid).delete()
            self.redirectUrl="/admin/pagelist/"

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):

            pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

            pageInfo=self.GetPage(pid)
            if pageInfo is None:
                pageInfo=Page()
          
            SetPageValues(self.request,pageInfo)

            titlepic = self.GetFile("titlepic")
            if titlepic is not None:
                attachInfo=self.SaveFile(titlepic)

                pageInfo.titlepic=attachInfo.path
            else:
                pics=utility.GetImgSrc(pageInfo.content)
                if pics:
                    pageInfo.titlepic=pics[0]
                        
            pageInfo.save()

        return locals()

            
def SetPageValues(request,pageInfo):
   
    title = pub.GetPostData(request,'title')
    summary=pub.GetPostData(request,'summary')
    content = pub.GetPostData(request,'content')

    status = pub.GetPostData(request,'status')
    cancomment = pub.GetPostData(request,'cancomment')
    password = pub.GetPostData(request,'password')
    template=pub.GetPostData(request,"template","normal")
    sidebar=pub.GetPostData(request,"sidebar","normal")
    sidebarfloat=pub.GetPostData(request,"sidebarfloat","none")
   
    if summary=="":
        tempContent=utility.RemoveTags(content)
        summary=tempContent[0:200] if len(tempContent)>200 else tempContent
    else:
        summary=utility.RemoveTags(summary)
   

    pageInfo.title = title
    pageInfo.summary=summary
    pageInfo.content = content
    pageInfo.createtime=datetime.datetime.now()
    #titlestyle={}
    #titlestyle.setdefault("b",True)     #加粗
    #titlestyle.setdefault("i",True)     #斜体
    #titlestyle.setdefault("u",True)     #下划张
    #titlestyle.setdefault("c",True)     #颜色
    #pageInfo.views=0
    #pageInfo.comments=0
    #pageInfo.goods=0
    #pageInfo.bads=0
    pageInfo.status=True if status=="1" else False
   
    pageInfo.cancomment=cancomment
    pageInfo.password=password
    pageInfo.user_id=1
    pageInfo.username="aaa"
    pageInfo.template=template
    pageInfo.sidebar=sidebar
    pageInfo.sidebarfloat=sidebarfloat
  



    
    
    
    
    
    
    

