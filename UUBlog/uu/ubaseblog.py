#-*- coding:utf-8 -*-
import os
import importlib
import uuid
import datetime

from UUBlog import settings
from UUBlog.core.ubasetemplateView import UBaseTemplateView
from UUBlog.common import utility,pub

from UUBlog.models import Option,Category,Post,Page,Comment,Navigate,Sidebar,MyWidget,Attachment

class UBaseBlogView(UBaseTemplateView):
    
    def __init__(self, **kwargs):
        super(UBaseBlogView, self).__init__(**kwargs)

        self.sysTime = GetSysTime()
        self.options = {}
        self.user = None

        self.theme = "default"
        self.themeConfig = {}

    def InitValue(self):

        self.sysTime = GetSysTime()
        self.options = self.GetOptions()
        self.user = self.request.user
        
        self.theme = self.GetOption("theme", "default")
        themeModuleName = "%s.%s.%s" % ("UUBlog.templates.themes", self.theme, "config")
        self.themeConfig = importlib.import_module(themeModuleName).config

    def post_context_data(self, **kwargs):
        context = super(UBaseBlogView, self).post_context_data(**kwargs)
       
        self.InitValue()

        myContext = self.PostContext(**kwargs)
        self.AddVars(context, myContext)

        return context

    def get_context_data(self, **kwargs):
        context = super(UBaseBlogView, self).get_context_data(**kwargs)

        self.InitValue()

        myContext = self.GetContext(**kwargs)
        self.AddVars(context, myContext)

        return context

    def GetHookList(self, key):
        global G
        if key in G["hooks"]:
            return G["hooks"][key]
        return []
            
    

    #模块列表
    def GetWidgetList(self, sid="default", isRender=True):
        if sid is None or sid == "":
            sid ="default"

        #获取博客的widget
        myWidgetList = MyWidget.objects.order_by("-sortnum").filter(sidebar_id=sid)
            
        if not isRender:
            return myWidgetList

        global G
        retWidgetList = []

        for myWidget in myWidgetList:
            widgetName = myWidget.widget

            widgetValue={}

            widgetValue.setdefault("id", myWidget.id)
            widgetValue.setdefault("name", widgetName)
            widgetValue.setdefault("title", myWidget.title)
            widgetValue.setdefault("isshowtitle", myWidget.isshowtitle)
            params = utility.Json2Obj(myWidget.params)
            widgetValue.setdefault("params", params)

            data = utility.Json2Obj(myWidget.data)

            if widgetName in G["widgets"]:
                widgetModule = G["widgets"][widgetName]
                widgetView = widgetModule.config["view"]
                if widgetView and callable(widgetView):
                    data = widgetView(self, myWidget, params)

            widgetValue.setdefault("data", data)

            retWidgetList.append(widgetValue)

        return retWidgetList

    def GetWidget(self, widgetId):
        try:
            widgetInfo = MyWidget.objects.get(id=widgetId)
        except:
            widgetInfo = None
        return widgetInfo

    #导航
    def GetNavList(self, parentId=-1, position=None, align=None):
        navList = Navigate.objects.order_by("position", "-sortnum")
        if parentId > -1:
            navList = navList.filter(parent_id=parentId)
        if position:
            navList = navList.filter(position=position)
        if align:
            navList = navList.filter(align=align)
        return navList

    def BuildNavTreeHtml(self, pId, level=-1, theId=-1):
        navs = self.GetNavList(pId, 1)

        if navs is None or len(navs) == 0:
            return ""

        level+=1

        options=""
        if level>0:
            options="<ul class='navs_%s childNavs'>" %(level)

        for nav in navs:
            if nav.id==theId:
                continue

            options+="<li class='leval_%s' ><a href='%s' target='%s'>%s</a>" %(level,nav.url,nav.target,nav.alias)
            
            options+=self.BuildNavTreeHtml(nav.id,level,theId)

            options+="</li>"

        if level>0:
            options+="</ul>"
        return options

    def BuildNavTreeJs(self,pId,position,level=-1,theId=-1):
        navList=self.GetNavList(pId,position)

        if navList is None or len(navList)==0:
            return ""

        level+=1

        options ="data[%s]=[" %pId
        for nav in navList:
            if nav.id==theId:
                continue
            options+="[%s,%s,'%s','%s','%s',%s]," %(nav.parent_id,nav.id,nav.name,nav.alias,nav.url,nav.sortnum)
        options=options.rstrip(",")+"];"

        for nav in navList:
            if nav.id==theId:
                continue

            options+=self.BuildNavTreeJs(nav.id,position,level,theId)
        return options

    def GetNav(self,navId):
        try:
            navInfo=Navigate.objects.get(id=navId)
        except:
            navInfo=None
        return navInfo

    #文章分类
    def GetCatList(self,parentId=-1):

        categoryList=Category.objects.order_by("-sortnum")
        if parentId>-1:
            categoryList=categoryList.filter(parent_id=parentId)
        return categoryList

    def BuildCatTreeJs(self,pId,level=-1,theId=-1):
        catList=self.GetCatList(pId)

        if catList is None or len(catList)==0:
            return ""

        level+=1

        options="data[%s]=[" %pId
        for cat in catList:
            if cat.id==theId:
                continue
            options+="[%s,%s,'%s','%s',%s,%s,%s]," %(cat.parent_id,cat.id,cat.name,cat.alias,cat.posts,cat.sortnum,level)
        options=options.rstrip(",")+"];"

        for cat in catList:
            if cat.id==theId:
                continue

            options+=self.BuildCatTreeJs(cat.id,level,theId)
        return options

    def BuildCatTreeHtml(self,pId,level=-1):
        catList=self.GetCatList(pId)

        if catList is None or len(catList)==0:
            return ""

        level+=1

        options=""
        if level>0:
            options="<ul class='cats_%s childCats'>" %(level)

        for cat in catList:
            
            options+="<li class='leval_%s' ><a href='/cat/%s/' >%s</a>" %(level,cat.id,cat.name)
            
            options+=self.BuildCatTreeHtml(cat.id,level)

            options+="</li>"
        if level>0:
            options+="</ul>"
        return options

    def GetCat(self, catId):
        try:
            catInfo = Category.objects.get(id=catId)
        except:
            catInfo = None
        return catInfo

    #侧边栏
    def GetSidebarList(self):
        return Sidebar.objects.all()

    #文章列表
    def GetPostList(self, *orders, **kwargs):
        postList = Post.objects.all()
        if kwargs:
            postList = postList.filter(**kwargs)
        if orders:
            postList = postList.order_by(*orders)
        else:
            postList = postList.order_by("-createtime")

        return postList

    def GetPost(self, postId):
        try:
            postInfo = Post.objects.get(id=postId)
        except:
            postInfo = None
        return postInfo

    #页面列表
    def GetPageList(self, *orders, **kwargs):
        pageList = Page.objects.all()
        if kwargs:
            pageList = pageList.filter(**kwargs)
        if orders:
            pageList = pageList.order_by(*orders)
        else:
            pageList = pageList.order_by("-createtime")
        return pageList

    def GetPage(self, pageId):
        try:
            pageInfo = Page.objects.get(id=pageId)
        except:
            pageInfo = None
        return pageInfo

    #评论列表
    def GetCommentList(self, *orders, **kwargs):
        commentList = Comment.objects.all()
        if kwargs:
            commentList = commentList.filter(**kwargs)
        if orders:
            commentList = commentList.order_by(*orders)
        else:
            commentList = commentList.order_by("-createtime")
        return commentList

    def GetComment(self, commentId):
        try:
            commentInfo = Comment.objects.get(id=commentId)
        except:
            commentInfo = None
        return commentInfo

    #获取一个Option的值
    def GetOption(self, name, defaultValue=None):
        if name in self.options:
            return self.options[name]

        optionList = Option.objects.filter(name=name)
        if optionList:
            ret = optionList[0].value
            if ret == "" and defaultValue is not None:
                return defaultValue
            return ret
        return defaultValue

    #修改或增加（isCreate为True时）一个Option
    def UpdateOption(self, name, value="", isCreate=True):
        optionValue = self.GetOption(name)
        if optionValue and optionValue == value:
            return

        optionList = Option.objects.filter(name=name)
        
        if optionList:
            optionInfo = optionList[0]
            optionInfo.value = value
            optionInfo.save()
        elif isCreate:
            optionInfo = Option()
            optionInfo.name = name
            optionInfo.value = value
            optionInfo.save()

    #获取所有的Option
    def GetOptions(self):
        ret = {}
        optionList = Option.objects.all()

        for optionInfo in optionList:
            ret.setdefault(optionInfo.name, optionInfo.value)

        return ret
         
    #添加访客
    def AddVisit(self, uid):
        pass
    def SaveFile(self, uploadFile):
        currentTime = datetime.datetime.now()

        #"\\attachment\\201309\\11" 
        #"1704"+guid
        path = "\\%s\\%s\\%s" % ("attachment", currentTime.strftime("%Y%m"), currentTime.strftime("%d"))
        fileName = "%s%s" % (currentTime.strftime("%H%M%S"), uuid.uuid1())

        uploadFileInfo = pub.SaveFile(uploadFile, path, fileName)
        attachInfo = Attachment()
        attachInfo.path = uploadFileInfo["path"]
        attachInfo.name = uploadFileInfo["newname"]
        attachInfo.title = uploadFileInfo["name"]
        attachInfo.description = uploadFileInfo["name"]
        attachInfo.extension = uploadFileInfo["ext"]

        filetype = 10
        if attachInfo.extension in self.options["filetype_image"]:
            filetype = 1
        elif attachInfo.extension in self.options["filetype_media"]:
            filetype = 2
        elif attachInfo.extension in self.options["filetype_file"]:
            filetype = 3
        attachInfo.filetype = filetype
        attachInfo.createtime = datetime.datetime.now()

        attachInfo.save()

        return attachInfo

def GetSysTime():
    return datetime.datetime.now()


G = {}
#{"addpost":[func1,func2,func3],}

def LoadWidgets():
    ret = {}
    dirPaths = os.listdir(settings.WidgetDir)
    for dirPath in dirPaths:
        if dirPath.find(".") > 0:
            continue
        moduleName = "%s.%s.%s.%s" % ("UUBlog", "widgets", dirPath, dirPath)
        module = importlib.import_module(moduleName)
        ret.setdefault(dirPath, module)
    return ret

G.setdefault("widgets", LoadWidgets())


def LoadPlugins():
    ret = {}
    
    dirPaths = os.listdir(settings.PluginDir)
    for dirPath in dirPaths:
        if dirPath.find(".") > 0:
            continue
        moduleName = "%s.%s.%s.%s" % ("UUBlog", "plugins", dirPath, dirPath)
        module = importlib.import_module(moduleName)
        ret.setdefault(dirPath, module)
    return ret

#G.setdefault("plugins",LoadPlugins())

def LoadHooks():
    ret = {}
    ret.setdefault("addpost", [1, 2, 3])
    ret.setdefault("deletepost", [3, 4, 5])
    return ret

G.setdefault("hooks", LoadHooks())






