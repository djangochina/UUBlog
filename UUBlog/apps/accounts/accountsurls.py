#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

from UUBlog import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^accounts/login/$',login,name='login'),
    #url(r'^accounts/logout/$',logout,name='logout'),
    #url(r'^test/$', 'apps.test.views.test'),
)

#帐户信息
urlpatterns += patterns('UUBlog.apps.accounts.views.viewaccounts',
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/register/$', 'register', name='register'),
     
    url(r'^(?P<uid>\d+)/accounts/$', 'base', name='accountsbase'),
    url(r'^(?P<uid>\d+)/accounts/avatar/$', 'avatar', name='accountsavatar'),
    url(r'^(?P<uid>\d+)/accounts/contact/$', 'contact', name='accountscontact'),
    url(r'^(?P<uid>\d+)/accounts/info/$', 'info', name='accountsinfo'),
    url(r'^(?P<uid>\d+)/accounts/security/$', 'security', name='accountssecurity'),
     
)


#urlpatterns += patterns('UUBlog.views.index',
#     url(r'^$', 'index', name='index'),
#)

##频道信息
#urlpatterns += patterns('UUBlog.apps.blog.views.viewchannel',
#     url(r'^channel/$', 'index',{"cid":1}, name='blogchannel'),
#     url(r'^channel/(?P<cid>\d+)$', 'index',name='blogchannel'),
    
#)
##文章管理
#urlpatterns += patterns('UUBlog.apps.blog.views.viewarticle',

#     #文章显示部分
#     url(r'^(?P<uid>\d+)/$', 'home', name='bloghome'),
#     url(r'^(?P<uid>\d+)/category/(?P<cid>\d+)$', 'blogpubcategory', name='blogcategory'),
#     url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', 'show', name='blogarticleshow'),


#     #文章管理部分
#     url(r'^(?P<uid>\d+)/pub/article/list/$', 'list',name='blogpubarticlelist'),
#     url(r'^(?P<uid>\d+)/pub/article/list/draft/$', 'listdraft',name='blogpubarticlelistdraft'),
#     url(r'^(?P<uid>\d+)/pub/article/list/category/(?P<cid>\d+)$', 'listcategory',name='blogpubarticlelistcategory'),
#     url(r'^(?P<uid>\d+)/pub/article/add/$', 'add',name='blogpubarticleadd'),
#     url(r'^(?P<uid>\d+)/pub/article/edit/(?P<aid>\d+)$', 'edit', name='blogpubarticleedit'),
#     url(r'^(?P<uid>\d+)/pub/article/delete/(?P<aid>\d+)$', 'delete', name='blogpubarticledelete'),
#)

##博客设置
#urlpatterns += patterns('UUBlog.apps.blog.views.viewblog',

#    url(r'^(?P<uid>\d+)/pub/setting/$', 'base', name='blogpubsetting'),
#    url(r'^(?P<uid>\d+)/pub/setting/$', 'domain', name='blogpubsettingdomain'),
#    url(r'^(?P<uid>\d+)/pub/setting/template/$', 'template', name='blogpubsettingtemplate'),
#    url(r'^(?P<uid>\d+)/pub/setting/style/$', 'style', name='blogpubsettingstyle'),
#)

##分类信息
#urlpatterns += patterns('UUBlog.apps.blog.views.viewcategory',
   
#     #分类管理部分
#     url(r'^(?P<uid>\d+)/pub/category/$', 'index', name='blogpubcategory'),
#     url(r'^(?P<uid>\d+)/pub/category/edit/(?P<cid>\d*)$', 'edit', name='blogpubcategoryedit'),
#     url(r'^(?P<uid>\d+)/pub/category/delete/(?P<cid>\d*)$', 'delete', name='blogpubcategorydelete'),
   
#)