#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
import UUBlog
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

urlpatterns += patterns('UUBlog.apps.blog.views.viewindex',
     url(r'^$', 'index', name='blogindex'),
)

#空间信息
urlpatterns += patterns('UUBlog.apps.blog.views.viewblog',
     url(r'^blog/$', 'index',{"tid":0}, name='blogblog'),
     url(r'^blog/suggest/$', 'index',{"order":"suggestes"},name='blogspacesuggest'),
     url(r'^blog/suggestnew/$', 'index',{"order":"lastsuggesttime"},name='blogspacesuggestnew'),
     url(r'^blog/follow/$', 'index',{"order":"follows"},name='blogspacefollow'),

     url(r'^blog/(?P<tid>\d+)/$', 'index',name='blogblog'),
     url(r'^blog/(?P<tid>\d+)/suggest/$', 'index',{"order":"suggestes"},name='blogspacesuggest'),
     url(r'^blog/(?P<tid>\d+)/suggestnew/$', 'index',{"order":"lastsuggesttime"},name='blogspacesuggestnew'),
     url(r'^blog/(?P<tid>\d+)/follow/$', 'index',{"order":"follows"},name='blogspacefollow'),
    
)

#ajax
urlpatterns += patterns('UUBlog.apps.blog.views.viewajax',
     url(r'^blogajax/followblog', 'followblog',{"bid":1}, name='blogajaxfollowblog'),
     url(r'^blogajax/suggestblog', 'suggestblog',{"bid":1}, name='blogajaxsuggestblog'),
     url(r'^blogajax/listenchannel$', 'listenchannel',{"cid":1}, name='blogajaxlistenchannel'),
    
)

#频道信息
urlpatterns += patterns('UUBlog.apps.blog.views.viewchannel',
     url(r'^channel/$', 'index',{"cid":1}, name='blogchannel'),
     url(r'^channel/my/$', 'my', name='blogchannelmy'),
     url(r'^channel/popular/$', 'popular', name='blogchannelpopular'),
     url(r'^channel/(?P<cid>\d+)/$', 'index',name='blogchannel'),
     url(r'^channel/(?P<cid>\d+)/(?P<c2id>\d+)/$', 'index',name='blogchannel'),
    
)

from UUBlog.apps.blog.views import viewarticle
#文章管理
urlpatterns += patterns('',

     url(r'^(?P<uid>\d+)/$', viewarticle.Home.as_view(), name='bloghome'),
     url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', viewarticle.Show.as_view(), name='blogarticleshow'),
)

#文章管理
urlpatterns += patterns('UUBlog.apps.blog.views.viewarticle',

     #文章显示部分
     #url(r'^(?P<uid>\d+)/$', 'home', name='bloghome'),
     url(r'^(?P<uid>\d+)/category/(?P<cid>\d+)$', 'category', name='blogcategory'),
     #url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', 'show', name='blogarticleshow'),


     #文章管理部分
     url(r'^(?P<uid>\d+)/pub/article/list/$', 'list',name='blogpubarticlelist'),
     url(r'^(?P<uid>\d+)/pub/article/list/draft/$', 'listdraft',name='blogpubarticlelistdraft'),
     url(r'^(?P<uid>\d+)/pub/article/list/category/(?P<cid>\d+)$', 'listcategory',name='blogpubarticlelistcategory'),
     url(r'^(?P<uid>\d+)/pub/article/add/$', 'add',name='blogpubarticleadd'),
     url(r'^(?P<uid>\d+)/pub/article/edit/(?P<aid>\d+)$', 'edit', name='blogpubarticleedit'),
     url(r'^(?P<uid>\d+)/pub/article/delete/(?P<aid>\d+)$', 'delete', name='blogpubarticledelete'),
)



#分类信息
urlpatterns += patterns('UUBlog.apps.blog.views.viewcategory',
   
     #分类管理部分
     url(r'^(?P<uid>\d+)/pub/category/$', 'index', name='blogpubcategory'),
     url(r'^(?P<uid>\d+)/pub/category/edit/(?P<cid>\d*)$', 'edit', name='blogpubcategoryedit'),
     url(r'^(?P<uid>\d+)/pub/category/delete/(?P<cid>\d*)$', 'delete', name='blogpubcategorydelete'),
   
)

#博客设置
urlpatterns += patterns('UUBlog.apps.blog.views.viewblog',

    url(r'^(?P<uid>\d+)/pub/setting/$', 'base', name='blogpubsetting'),
    url(r'^(?P<uid>\d+)/pub/setting/avatar', 'avatar', name='blogpubsettingavatar'),
    url(r'^(?P<uid>\d+)/pub/setting/module', 'module', name='blogpubsettingmodule'),
    url(r'^(?P<uid>\d+)/pub/setting/domain$', 'domain', name='blogpubsettingdomain'),
    url(r'^(?P<uid>\d+)/pub/setting/template/$', 'template', name='blogpubsettingtemplate'),
    url(r'^(?P<uid>\d+)/pub/setting/style/$', 'style', name='blogpubsettingstyle'),
)










