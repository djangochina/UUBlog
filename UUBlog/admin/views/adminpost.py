#-*- coding:utf-8 -*-
import datetime

from UUBlog.common import utility,pub

from UUBlog.models import Post,Category


from UUBlog.uu.ubaseadmin import UBaseAdminView

#post manager
class PostListView(UBaseAdminView):

    def GetContext(self, **kwargs):
        catid=utility.ToInt(self.GetGetData("catid"),-1)
        istop=utility.ToInt(self.GetGetData("istop"),-1)
        status=utility.ToInt(self.GetGetData("status"),-1)
        time=utility.ToInt(self.GetGetData("time"),-1)
        keywords=self.GetGetData("keywords")

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)

        postList=Post.objects.order_by("-createtime")

        if catid>-1:
            postList=postList.filter(category_id=catid)
        if istop>-1:
            postList=postList.filter(istop=istop)
        if status>-1:
            postList=postList.filter(status=status)
        if time>-1:
            startTime=datetime.datetime.now()-datetime.timedelta(time)
            postList=postList.filter(createtime__gte=startTime)
        if keywords!="":
            postList=postList.filter(title__icontains=keywords)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("admin_pagesize",10)

        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pagedObject=postList

        self.SetTemplateName("postlist")
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('okFilter'):
            catId=self.GetPostData("catTree")
            status=self.GetPostData("status")
            istop=self.GetPostData("istop")
            time=self.GetPostData("time")
            keywords=self.GetPostData("keywords")

            self.currentQueryString="catid=%s&status=%s&istop=%s&time=%s&keywords=%s" %(catId,status,istop,time,keywords)
            self.redirectUrl="/admin/postlist/"
            
        return locals()

#edit post or create new post
class PostEditView(UBaseAdminView):

    def DefaultTemplateName(self):
        return "post"

    def GetContext(self, **kwargs):
        action = self.GetGetData("action", "edit")
        pid = utility.ToInt(utility.GetDicData(kwargs, "pid"), 0)

        if action == "edit":
            if pid > 0:
                postInfo = self.GetPost(pid)
                if postInfo is None:
                    self.message = "文章不存在"
                    self.SetTemplateName("message")
                    self.redirectUrl = "/admin/postlist/"
                    self.autoRedirect = False
                    return locals()
            else:
                postInfo=Post()

            catTree = "var data=Array();"
            catTree += self.BuildCatTreeJs(0, -1, -1)

        else:
            if action == "delete":
                Post.objects.filter(id=pid).delete()
            self.redirectUrl = "/admin/postlist/"
            self.currentQueryString = self.BuildQueryString(self.currentQueryDic, action=None)

        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):

            pid = utility.ToInt(utility.GetDicData(kwargs, "pid"), 0)
            catId = utility.ToInt(self.GetPostData("catTree"), 0)
            oldCatId = None

            postInfo = self.GetPost(pid)
            if postInfo is None:
                postInfo = Post()
            else:
                oldCatId = postInfo.category_id
            
            postInfo.category_id = catId
            
            SetPostValues(self.request, postInfo)

            titlepic = self.GetFile("titlepic")
            if titlepic is not None:
                attachInfo = self.SaveFile(titlepic)

                postInfo.titlepic = attachInfo.path

            else:
                pics = utility.GetImgSrc(postInfo.content)
                if pics:
                    postInfo.titlepic = pics[0]
                        
            postInfo.save()

            #更新分类统计信息 不是默认分类并且是发布的文章
            if catId != 0 and postInfo.status:
                categoryInfo = self.GetCat(catId)
                categoryInfo.posts += 1
                categoryInfo.save()
            if oldCatId:

                if oldCatId == catId:
                    pass
                else:

                    pass
                
            else:
                pass

        return locals()

            
def SetPostValues(request, postInfo):
   
    title = pub.GetPostData(request,'title')
    summary = pub.GetPostData(request,'summary')
    content = pub.GetPostData(request,'content')

    tags = pub.GetPostData(request,'tags')
    status = pub.GetPostData(request,'status')
    createtime = pub.GetPostData(request,"createtime")

    cancomment = pub.GetPostData(request,'cancomment')
    istop=pub.GetPostData(request,"istop",False)
    password = pub.GetPostData(request,'password')
    template=pub.GetPostData(request,"template","normal")
    sidebar=pub.GetPostData(request,"sidebar","normal")
    sidebarfloat=pub.GetPostData(request,"sidebarfloat","none")

    if summary == "":
        tempContent = utility.RemoveTags(content)
        summary = tempContent[0:200] if len(tempContent) > 200 else tempContent
    else:
        summary = utility.RemoveTags(summary)
   

    postInfo.title = title
    postInfo.tags=tags
    postInfo.summary=summary
    postInfo.content = content
    postInfo.createtime=createtime
    #titlestyle={}
    #titlestyle.setdefault("b",True)     #加粗
    #titlestyle.setdefault("i",True)     #斜体
    #titlestyle.setdefault("u",True)     #下划张
    #titlestyle.setdefault("c",True)     #颜色
    #postInfo.views=0
    #postInfo.comments=0
    #postInfo.goods=0
    #postInfo.bads=0
    postInfo.status=True if status=="1" else False
   
    postInfo.cancomment=cancomment
    postInfo.istop=istop
    postInfo.password=password
    postInfo.user_id=1
    postInfo.username="aaa"
    postInfo.template=template
    postInfo.sidebar=sidebar
    postInfo.sidebarfloat=sidebarfloat



    
    
    
    
    
    
    
    
    
