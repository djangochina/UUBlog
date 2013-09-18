#-*- coding:utf-8 -*-
from UUBlog.common import utility
from UUBlog.models import Category
from UUBlog.uu.ubaseadmin import UBaseAdminView


class CatManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        catTree="var data=Array();"
        catTree+=self.BuildCatTreeJs(0,-1,-1)

        catList=self.GetCatList()

        self.SetTemplateName("catlist")
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData('ok'):
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias",name)
            sortnum=utility.ToInt(self.GetPostData("sortnum"))
            template=self.GetPostData("template","normal")
            sidebar=self.GetPostData("sidebar","normal")
            sidebarfloat=self.GetPostData("sidebarfloat","none")

            catInfo=Category()
            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0
            catInfo.template=template
            catInfo.sidebar=sidebar
            catInfo.sidebarfloat=sidebarfloat

            catInfo.save()
        if self.HasPostData("okSort"):
            for key,value in self.request.POST.items():
                if key.find("item_sortnum_")==0:
                    dot=key.rfind("_")
                    catId=key[dot+1:]
                    Category.objects.filter(id=catId).update(sortnum=utility.ToInt(value,0))
        return locals()

class CatEditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        cid=int(kwargs.get("cid",0))

        action=self.GetGetData("action","edit")

        if action=="edit":
            if cid>0:
                catInfo=self.GetCat(cid)
                if catInfo is None:
                    self.message="分类不存在"
                    self.SetTemplateName("message")
                    self.redirectUrl="/admin/catlist/"
                    self.autoRedirect=False
                    return locals()
            else:
                catInfo=Category()
            catTree="var data=Array();"
            catTree+=self.BuildCatTreeJs(0,-1,cid)
            self.SetTemplateName("cat")

        else:
            if action=="delete":
                catInfo=self.GetCat(cid)
                if catInfo is not None:
                    Category.objects.filter(id=cid).delete()
                    Category.objects.filter(parent_id=cid).update(parent_id=catInfo.parent_id)
            self.redirectUrl="/admin/catlist/"

        return locals()

    def PostContext(self, **kwargs):
       
        if self.HasPostData('ok'):
            cid=int(kwargs.get("cid",0))
            parentId=self.GetPostData("parentId",0)
            name=self.GetPostData("name")
            alias=self.GetPostData("alias")
            sortnum=self.GetPostData("sortnum",0)
            template=self.GetPostData("template","normal")
            sidebar=self.GetPostData("sidebar","normal")
            sidebarfloat=self.GetPostData("sidebarfloat","none")

            catInfo=self.GetCat(cid)
            if catInfo is None:
                catInfo=Category()

            catInfo.parent_id=parentId
            catInfo.name=name
            catInfo.alias=alias
            catInfo.sortnum=0 if sortnum=="" else sortnum
            catInfo.articles=0
            catInfo.template=template
            catInfo.sidebar=sidebar
            catInfo.sidebarfloat=sidebarfloat

            catInfo.save()
        
        self.redirectUrl="/admin/catlist"
        return locals()




    