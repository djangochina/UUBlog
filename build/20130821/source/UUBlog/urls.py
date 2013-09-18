#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

import settings
from django.contrib import admin
from UUBlog.views import view
from UUBlog.init import *
from UUBlog.admin.views import adminview,adminpost,adminpage
from UUBlog.admin.views import adminsetting


admin.autodiscover()



urlpatterns = patterns('',

)


urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
     url(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
#urlpatterns += patterns('',
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#)

from UUBlog.admin.views import admincategory,admintag,admintheme

urlpatterns += patterns('',
    url(r'^admin/$', adminview.IndexView.as_view(),name="admin_index"),

   

   
)
#内容
urlpatterns += patterns('',

    #文章
    url(r'^admin/postlist/$', adminpost.PostListView.as_view(),name="admin_post_manager"),
    url(r'^admin/post/$', adminpost.PostEditView.as_view(),name="admin_post_edit"),
    url(r'^admin/post/(?P<pid>\d+)/$', adminpost.PostEditView.as_view(),name="admin_post_edit"),

    #文章分类
    url(r'^admin/catlist/$', admincategory.CatManagerView.as_view(),name="admin_cat_manager"),
    url(r'^admin/cat/$', admincategory.CatEditView.as_view(),name="admin_cat_edit"),
    url(r'^admin/cat/(?P<cid>\d+)/$', admincategory.CatEditView.as_view(),name="admin_cat_edit"),

    url(r'^admin/tag/$', admintag.ManagerView.as_view(),name="admin_tag_manager"),


    #页面
    url(r'^admin/pagelist/$', adminpage.PageListView.as_view(),name="admin_page_manager"),
    url(r'^admin/page/$', adminpage.PageEditView.as_view(),name="admin_page_edit"),
    url(r'^admin/page/(?P<pid>\d+)/$', adminpage.PageEditView.as_view(),name="admin_page_edit"),

)

#外观
urlpatterns += patterns('',
    

    url(r'^admin/theme/$', admintheme.ThemeManagerView.as_view(),name="admin_theme_manager"),

    url(r'^admin/widgetlist/$', admintheme.WidgetManagerView.as_view(),name="admin_widget_manager"),
    url(r'^admin/widgetlist/(?P<name>.+)', admintheme.WidgetManagerView.as_view(),name="admin_widget_manager"),
    url(r'^admin/widget/(?P<wid>\d+)$', admintheme.WidgetEditView.as_view(),name="admin_widget_edit"),

    url(r'^admin/navlist/position/$', admintheme.NavManagerView.as_view(),{"p":1},name="admin_nav_manager"),
    url(r'^admin/navlist/position/(?P<p>\d+)/$', admintheme.NavManagerView.as_view(),name="admin_nav_manager"),
    url(r'^admin/nav/position/(?P<p>\d+)/(?P<nid>\d+)/$', admintheme.NavEditView.as_view(),name="admin_nav_manager"),
    
    url(r'^admin/file/$', admintheme.FileManagerView.as_view(),name="admin_file_manager"),
)


#博客设置
urlpatterns += patterns('',

    url(r'^admin/setting/$', adminsetting.BaseView.as_view(), name='admin_setting_base'),
    url(r'^admin/setting/avatar/$', adminsetting.AvatarView.as_view(), name='admin_setting_avatar'),
    url(r'^admin/setting/comment/$', adminsetting.CommentView.as_view(), name='admin_setting_comment'),
    url(r'^admin/setting/content/$', adminsetting.ContentView.as_view(), name='admin_setting_content'),
    url(r'^admin/setting/other/$', adminsetting.OtherView.as_view(), name='admin_setting_other'),
)

#首页
urlpatterns += patterns('',
    url(r'^$', view.IndexView.as_view(), name='index'),
    url(r'^list/(?P<page>\d+)/$', view.ListView.as_view(), name='list'),
    url(r'^cat/(?P<cid>\d+)/$', view.ListView.as_view(), name='category'),
    url(r'^tag/(?P<tid>\d+)/$', view.ListView.as_view(), name='tag'),
    url(r'^post/(?P<pid>\d+)/$', view.PostView.as_view(), name='post'),
    url(r'^page/(?P<pid>\d+)/$', view.PageView.as_view(), name='page'),
)


    
def AddWidgetUrls():
    

    global G

    var =GetSysTime()
    p=patterns("")
    
    aaa=G

    for key,module in G["widgets"].items():
        p.append(url(r'^widget/'+key+'/(?P<wid>\d+)/$', module.config["setting"].as_view(), name='widget'))
    return p

urlpatterns += AddWidgetUrls()