#-*- coding:utf-8 -*-

from UUBlog.uu.ubaseadmin import UBaseAdminView

#用户博客首页
class IndexView(UBaseAdminView):

    def GetContext(self, **kwargs):

        myWidgetList=self.GetWidgetList()
       
        postList=self.GetPostList()

        self.SetTemplateName("index")
        return locals()



  



    
    
    
    
    
    
    
    

