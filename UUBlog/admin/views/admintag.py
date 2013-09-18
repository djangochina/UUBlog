#-*- coding:utf-8 -*-



from UUBlog.models import Category
from UUBlog.uu.ubaseadmin import UBaseAdminView


class ManagerView(UBaseAdminView):
    def GetContext(self, **kwargs):

        categoryList=self.GetCatList()

        self.template_name="admin/tag.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData('ok'):
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category()
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.save()

        return locals()

class EditView(UBaseAdminView):
    

    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        categoryInfo=Category.objects.get(id=cid)

        self.template_name="blog/pub/category.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))

        if self.HasPostData('ok'):
            
            name=self.GetPostData("name")
            sortnum=self.GetPostData("sortnum")
            isnav=self.GetPostData("isnav",False)

            categoryInfo=Category.objects.get(id=cid)
            categoryInfo.name=name
            categoryInfo.sortnum=sortnum
            categoryInfo.isnav=1 if isnav else 0

            categoryInfo.save()

        return locals()

class DeleteView(UBaseAdminView):
    
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        cid=int(kwargs.get("cid",0))
      
        categoryInfo=Category.objects.get(id=cid)
        categoryInfo.delete()


        self.template_name="blog/pub/category.html"

        return locals()


    