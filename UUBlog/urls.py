#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

import settings
from django.contrib import admin
from UUBlog.views import view

from UUBlog.admin.views import admincategory,admintag,admintheme,adminview,adminpost,adminpage,adminattachment,adminsetting,adminnav,adminsidebar, adminwidget, adminaccount


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



urlpatterns += patterns('',
    url(r'^admin/login/$', adminaccount.LoginView.as_view(),name="login"),
    url(r'^admin/logout/$', adminaccount.LogoutView.as_view(),name="logout"),
)
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

    #Tag
    url(r'^admin/tag/$', admintag.ManagerView.as_view(),name="admin_tag_manager"),


    #页面
    url(r'^admin/pagelist/$', adminpage.PageListView.as_view(),name="admin_page_manager"),
    url(r'^admin/page/$', adminpage.PageEditView.as_view(),name="admin_page_edit"),
    url(r'^admin/page/(?P<pid>\d+)/$', adminpage.PageEditView.as_view(),name="admin_page_edit"),

)

#附件
urlpatterns += patterns('',
    url(r'^admin/attachmentlist/$', adminattachment.AttachmentManagerView.as_view(),name="admin_attach_manager"),
    url(r'^admin/attachment/$', adminattachment.AttachmentEditView.as_view(),name="admin_attach_edit"),
    url(r'^admin/attachment/(?P<aid>\d+)/$', adminattachment.AttachmentEditView.as_view(),name="admin_attach_edit"),
    url(r'^admin/attachment/upload/$', adminattachment.AttachmentUploadView.as_view(),name="admin_attach_upload"),

)

#外观
urlpatterns += patterns('',
    
    url(r'^admin/theme/$', admintheme.ThemeManagerView.as_view(),name="admin_theme_manager"),
    url(r'^admin/headerstyle/$', admintheme.HeaderStyleView.as_view(),name="admin_header_style"),
    url(r'^admin/backgroundstyle/$', admintheme.BackgroundStyleView.as_view(),name="admin_background_style"),
  

    #菜单
    url(r'^admin/navlist/position/$', adminnav.NavManagerView.as_view(),{"p":1},name="admin_nav_manager"),
    url(r'^admin/navlist/position/(?P<p>\d+)/$', adminnav.NavManagerView.as_view(),name="admin_nav_manager"),
    url(r'^admin/nav/position/(?P<p>\d+)/(?P<nid>\d+)/$', adminnav.NavEditView.as_view(),name="admin_nav_manager"),
    
)

#侧边栏及小工具
urlpatterns += patterns('',
    
    url(r'^admin/sidebarlist/$', adminsidebar.SidebarManagerView.as_view(),name="admin_sidebar_manager"),
    url(r'^admin/sidebar/(?P<sid>\w+)/$', adminsidebar.SidebarEditView.as_view(),name="admin_sidebar_edit"),
    url(r'^admin/sidebar/$', adminsidebar.SidebarEditView.as_view(),name="admin_sidebar_edit"),

    url(r'^admin/widgetlist/$', adminwidget.WidgetManagerView.as_view(),name="admin_widget_manager"),
    url(r'^admin/widgetlist/(?P<sid>.+)/$', adminwidget.WidgetManagerView.as_view(),name="admin_widget_manager"),

    url(r'^admin/widget/(?P<wid>\d+)/$', adminwidget.WidgetSettingView, name='admin_widget_edit'),
    #url(r'^admin/widget/*/$', adminwidget.WidgetSettingView, name='admin_widget_edit'),
    url(r'^admin/widget/(?P<sid>.+)/(?P<wid>\d+)/$', adminwidget.WidgetEditView.as_view(),name="admin_widget_edit"),

)
urlpatterns += patterns('',

)
#用户设置
urlpatterns += patterns('',
                        
    url(r'^admin/account/security/$', adminaccount.SecurityView.as_view(), name='admin_account_security'),
    
)

#博客设置
urlpatterns += patterns('',

    url(r'^admin/setting/$', adminsetting.BaseView.as_view(), name='admin_setting_base'),

    url(r'^admin/setting/comment/$', adminsetting.CommentView.as_view(), name='admin_setting_comment'),
    url(r'^admin/setting/content/$', adminsetting.ContentView.as_view(), name='admin_setting_content'),
    url(r'^admin/setting/attachment/$', adminsetting.AttachmentView.as_view(), name='admin_setting_attach'),
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
    url(r'^search/$', view.SearchView.as_view(), name='search'),
    url(r'^close/$', view.CloseView.as_view(), name='close'),
)

