#-*- coding:utf-8 -*-
import datetime
from UUBlog.common import pub,utility
from UUBlog.models import Comment
from UUBlog.uu.ubaseuser import UBaseUserView


#用户博客首页
class IndexView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(IndexView, self).GetContext(**kwargs)

        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("index_pagesize",20)

        postList=self.GetPostList(status=1)
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList
       
        
        self.templateName="index_"+self.GetOption("index_template","normal")
        self.sidebar=self.GetOption("index_sidebar","normal")
        self.sidebarFloat=self.GetOption("index_sidebar_float","none")

        self.SetTemplateAndSidebar()

        return locals()

#列表浏览
class ListView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(ListView, self).GetContext(**kwargs)

        cid= utility.ToInt(utility.GetDicData(kwargs,"cid"),0)
        tid= utility.ToInt(utility.GetDicData(kwargs,"tid"),0)
        
        if cid>0:
            catInfo=self.GetCat(cid)
            if catInfo is None:
                self.SetMessageTemplate("分类不存在")
                return locals()

            pageSize=self.GetOption("cat_pagesize",20)

            postList=self.GetPostList(status=1,category_id=cid)

            
            self.templateName="cat_"+catInfo.template
            self.sidebar=catInfo.sidebar
            self.sidebarFloat=catInfo.sidebarfloat

        elif tid>0:
            postList=self.GetPostList(status=1)
            #pageSize=self.GetOption("tag_pagesize",10)
            #postList=postList.filter(category_id=cid)
            #self.sidebar=catInfo.sidebar
            #self.templateName="tag_"+catInfo.template

            pass
        else:
            self.redirectUrl="/"
            return locals()

        pageIndex=utility.ToInt(self.GetGetData("page"),1)

        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList

        self.SetTemplateAndSidebar()
        return locals()

#列表浏览
class SearchView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(SearchView, self).GetContext(**kwargs)

        word=self.GetGetData("word")
        
        pageIndex=utility.ToInt(self.GetGetData("page"),1)
        pageSize=self.GetOption("search_pagesize",20)

        postList=self.GetPostList(status=1,title__icontains=word)
        postList=pub.GetPagedObject(postList,pageIndex,pageSize)
        pageObject=postList

        
        self.templateName="search_"+self.GetOption("search_template","normal")
        self.sidebar=self.GetOption("search_sidebar","normal")
        self.sidebarFloat=self.GetOption("search_sidebar_float","none")

        self.SetTemplateAndSidebar()
        return locals()

#文章页面
class PostView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(PostView, self).GetContext(**kwargs)

        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)
    
        postInfo=self.GetPost(pid)
        if postInfo is None:
            self.SetMessageTemplate("此文章不存在")
            return locals()

        #更新文章浏览量
        postInfo.views+=1
        postInfo.save()

        hookList=self.GetHookList("post_BeforShow")
        for hook in hookList:
            if callable(hook):
                postInfo=hook(postInfo)
        
        objInfo=postInfo
        commentList=self.GetCommentList(obj_id=pid)

        comment_paging = self.GetOption("comment_paging","True")
        if comment_paging=="True":
            pageIndex=utility.ToInt(self.GetGetData("page"),1)
            pageSize=self.GetOption("comment_pagesize",20)
        
            commentList=pub.GetPagedObject(commentList,pageIndex,pageSize)
            pageObject=commentList
            

        
        self.templateName="post_"+postInfo.template
        self.sidebar=postInfo.sidebar
        self.sidebarFloat=postInfo.sidebarfloat

        self.SetTemplateAndSidebar()
        return locals()

    def PostContext(self, **kwargs):
        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

        if self.HasPostData("ok") and pid>0:
            postInfo=self.GetPost(pid)
            if postInfo is None:
                
                return locals()

            username = self.GetPostData('username')
            email = self.GetPostData('email')
            title = self.GetPostData('title')
            content = self.GetPostData('content')
            
            commentInfo=Comment()
            commentInfo.obj_id=pid
            commentInfo.obj_type="post"
            commentInfo.title=title
            commentInfo.content=content
            commentInfo.createtime=datetime.datetime.now()
            commentInfo.user_id=0
            commentInfo.username=username
            commentInfo.email=email

            commentInfo.save()

            postInfo.comments+=1
            postInfo.save()

#文章页面
class PageView(UBaseUserView):
    
    def GetContext(self, **kwargs):
        super(PageView, self).GetContext(**kwargs)

        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

        pageInfo=self.GetPage(pid)
        if pageInfo is None:
            self.SetMessageTemplate("此页面不存在")
            return locals()

        #更新文章浏览量
        pageInfo.views+=1
        pageInfo.save()

        
        objInfo=pageInfo
        commentList=self.GetCommentList(obj_id=pid)

        comment_paging = self.GetOption("comment_paging","True")
        if comment_paging=="True":
            pageIndex=utility.ToInt(self.GetGetData("page"),1)
            pageSize=self.GetOption("comment_pagesize",20)
        
            commentList=pub.GetPagedObject(commentList,pageIndex,pageSize)
            pageObject=commentList


        
        self.templateName="page_"+pageInfo.template
        self.sidebar=pageInfo.sidebar
        self.sidebarFloat=pageInfo.sidebarfloat

        self.SetTemplateAndSidebar()
        return locals()

    def PostContext(self, **kwargs):
        pid= utility.ToInt(utility.GetDicData(kwargs,"pid"),0)

        if self.HasPostData("ok") and pid>0:
            pageInfo=self.GetPage(pid)
            if pageInfo is None:
                return locals()

            username = self.GetPostData('username')
            email = self.GetPostData('email')
            title = self.GetPostData('title')
            content = self.GetPostData('content')
            
            commentInfo=Comment()
            commentInfo.obj_id=pid
            commentInfo.obj_type="page"
            commentInfo.title=title
            commentInfo.content=content
            commentInfo.createtime=datetime.datetime.now()
            commentInfo.user_id=0
            commentInfo.username=username
            commentInfo.email=email

            commentInfo.save()

            pageInfo.comments+=1
            pageInfo.save()    
            
            
class CloseView(UBaseUserView):

    def GetContext(self, **kwargs):
        super(CloseView, self).GetContext(**kwargs)

        close_info=utility.GetDicData(self.options,"close_info","")
        self.SetTemplateName("close")

        return locals()            
    
    