#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
import UUBlog
from UUBlog import settings
from django.contrib import admin
from UUBlog.apps.blog.views import viewarticle,viewblog,viewchannel,viewindex,viewcategory


admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^accounts/login/$',login,name='login'),
    #url(r'^accounts/logout/$',logout,name='logout'),
    #url(r'^test/$', 'apps.test.views.test'),
)

urlpatterns += patterns('',
     url(r'^$', viewindex.IndexView.as_view(), name='blogindex'),
)

#空间信息
urlpatterns += patterns('',
     url(r'^blog/$', viewblog.IndexView.as_view(),{"tid":0,"order":"suggestes"}, name='blogblog'),
     url(r'^blog/suggest/$', viewblog.IndexView.as_view(),{"order":"suggestes"},name='blogspacesuggest'),
     url(r'^blog/suggestnew/$', viewblog.IndexView.as_view(),{"order":"lastsuggesttime"},name='blogspacesuggestnew'),
     url(r'^blog/follow/$', viewblog.IndexView.as_view(),{"order":"follows"},name='blogspacefollow'),

     url(r'^blog/(?P<tid>\d+)/$', viewblog.IndexView.as_view(),{"order":"suggestes"},name='blogblog'),
     url(r'^blog/(?P<tid>\d+)/suggest/$', viewblog.IndexView.as_view(),{"order":"suggestes"},name='blogspacesuggest'),
     url(r'^blog/(?P<tid>\d+)/suggestnew/$', viewblog.IndexView.as_view(),{"order":"lastsuggesttime"},name='blogspacesuggestnew'),
     url(r'^blog/(?P<tid>\d+)/follow/$', viewblog.IndexView.as_view(),{"order":"follows"},name='blogspacefollow'),
    
)



#ajax
urlpatterns += patterns('UUBlog.apps.blog.views.viewajax',
     url(r'^blogajax/followblog', 'followblog',{"bid":1}, name='blogajaxfollowblog'),
     url(r'^blogajax/suggestblog', 'suggestblog',{"bid":1}, name='blogajaxsuggestblog'),
     url(r'^blogajax/listenchannel$', 'listenchannel',{"cid":1}, name='blogajaxlistenchannel'),
    
)

#频道信息
urlpatterns += patterns('',
     url(r'^channel/$', viewchannel.IndexView.as_view(),{"cid":1}, name='blogchannel'),
     #url(r'^channel/my/$', 'my', name='blogchannelmy'),
     #url(r'^channel/popular/$', 'popular', name='blogchannelpopular'),
     url(r'^channel/(?P<cid>\d+)/$', viewchannel.IndexView.as_view(),name='blogchannel'),
     url(r'^channel/(?P<cid>\d+)/(?P<c2id>\d+)/$', viewchannel.IndexView.as_view(),name='blogchannel'),
    
)
#频道信息
urlpatterns += patterns('UUBlog.apps.blog.views.viewchannel',
     #url(r'^channel/$', 'index',{"cid":1}, name='blogchannel'),
     url(r'^channel/my/$', 'my', name='blogchannelmy'),
     url(r'^channel/popular/$', 'popular', name='blogchannelpopular'),
     #url(r'^channel/(?P<cid>\d+)/$', 'index',name='blogchannel'),
     #url(r'^channel/(?P<cid>\d+)/(?P<c2id>\d+)/$', 'index',name='blogchannel'),
    
)



#用户博客首页及文章显示
urlpatterns += patterns('',
     url(r'^(?P<uid>\d+)/$', viewarticle.HomeView.as_view(), name='bloghome'),
     url(r'^(?P<uid>\d+)/category/(?P<cid>\d+)$', viewarticle.CategoryView.as_view(), name='blogcategory'),
     url(r'^(?P<uid>\d+)/tag/(?P<tid>\d+)$', viewarticle.TagView.as_view(), name='blogcategory'),
     url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', viewarticle.ShowView.as_view(), name='blogarticleshow'),
)

#文章管理
urlpatterns += patterns('',

     url(r'^(?P<uid>\d+)/pub/article/list/$', viewarticle.PubListView.as_view(),name='blogpubarticlelist'),
     url(r'^(?P<uid>\d+)/pub/article/list/draft/$', viewarticle.PubListView.as_view(),{"draft":True},name='blogpubarticlelistdraft'),
     url(r'^(?P<uid>\d+)/pub/article/list/category/(?P<cid>\d+)$', viewarticle.PubListView.as_view(),name='blogpubarticlelistcategory'),
     url(r'^(?P<uid>\d+)/pub/article/add/$', viewarticle.ArticleAddView.as_view(),name='blogpubarticleadd'),
     url(r'^(?P<uid>\d+)/pub/article/edit/(?P<aid>\d+)$', viewarticle.ArticleEditView.as_view(), name='blogpubarticleedit'),
     url(r'^(?P<uid>\d+)/pub/article/delete/(?P<aid>\d+)$', viewarticle.ArticleDeleteView.as_view(), name='blogpubarticledelete'),
)



#分类信息
urlpatterns += patterns('',
   
     #分类管理部分
     url(r'^(?P<uid>\d+)/pub/category/$', viewcategory.IndexView.as_view(), name='blogpubcategory'),
     url(r'^(?P<uid>\d+)/pub/category/edit/(?P<cid>\d*)$', viewcategory.CategoryEditView.as_view(), name='blogpubcategoryedit'),
     url(r'^(?P<uid>\d+)/pub/category/delete/(?P<cid>\d*)$', viewcategory.CategoryDeleteView.as_view(), name='blogpubcategorydelete'),
   
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










