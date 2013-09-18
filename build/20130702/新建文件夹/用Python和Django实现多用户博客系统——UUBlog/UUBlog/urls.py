#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from UUBlog.views import *
from UUBlog.models import *
import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^accounts/login/$',login,name='login'),
    #url(r'^accounts/logout/$',logout,name='logout'),
    
)

urlpatterns += patterns('',
     url(r'^$', 'UUBlog.viewsindex.index', name='index'),
     url(r'^channel/$', 'UUBlog.viewsindex.channel',{"cid":1}, name='channel'),
     url(r'^test/$', 'UUBlog.viewsindex.test', name='test'),
     url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
     url(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

)

urlpatterns += patterns('',
    # Examples:
     url(r'^$', 'index', name='index'),
     
     url(r'^channel/(?P<cid>\d+)$', 'UUBlog.viewsindex.channel', name='channel'),
     
     url(r'^accounts/login/$', 'UUBlog.viewsuser.login', name='login'),
     url(r'^accounts/logout/$', 'UUBlog.viewsuser.logout', name='logout'),
     url(r'^accounts/register/$', 'UUBlog.viewsuser.register', name='register'),
     
     url(r'^(?P<uid>\d+)/pub/accounts/$', 'UUBlog.viewsuserprofile.base', name='profilebase'),
     url(r'^(?P<uid>\d+)/pub/accounts/avatar/$', 'UUBlog.viewsuserprofile.avatar', name='profileavatar'),
     url(r'^(?P<uid>\d+)/pub/accounts/contact/$', 'UUBlog.viewsuserprofile.contact', name='profilecontact'),
     url(r'^(?P<uid>\d+)/pub/accounts/info/$', 'UUBlog.viewsuserprofile.info', name='profileinfo'),
     url(r'^(?P<uid>\d+)/pub/accounts/security/$', 'UUBlog.viewsuserprofile.security', name='profilesecurity'),
     
     url(r'^(?P<uid>\d+)/pub/config/$', 'UUBlog.viewsblog.blog', name='configblog'),
    


     #文章显示部分
     url(r'^(?P<uid>\d+)/$', 'UUBlog.viewsarticle.home', name='userhome'),
     url(r'^(?P<uid>\d+)/category/(?P<cid>\d+)$', 'UUBlog.viewsarticle.category', name='articlecategory'),
     url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', 'UUBlog.viewsarticle.show', name='articleshow'),

     #文章管理部分
     url(r'^(?P<uid>\d+)/pub/article/list/$', 'UUBlog.viewsarticle.list',name='articlelist'),
     url(r'^(?P<uid>\d+)/pub/article/list/draft/$', 'UUBlog.viewsarticle.listdraft',name='articlelistdraft'),
     url(r'^(?P<uid>\d+)/pub/article/list/category/(?P<cid>\d+)$', 'UUBlog.viewsarticle.listcategory',name='articlelistcategory'),
     url(r'^(?P<uid>\d+)/pub/article/add/$', 'UUBlog.viewsarticle.add',name='articleadd'),
     url(r'^(?P<uid>\d+)/pub/article/edit/(?P<aid>\d+)$', 'UUBlog.viewsarticle.edit', name='articleedit'),
     url(r'^(?P<uid>\d+)/pub/article/delete/(?P<aid>\d+)$', 'UUBlog.viewsarticle.delete', name='articledelete'),

     #分类管理部分
     url(r'^(?P<uid>\d+)/pub/category/$', 'UUBlog.viewscategory.index', name='category'),
     url(r'^(?P<uid>\d+)/pub/category/edit/(?P<cid>\d*)$', 'UUBlog.viewscategory.edit', name='categoryedit'),
     url(r'^(?P<uid>\d+)/pub/category/delete/(?P<cid>\d*)$', 'UUBlog.viewscategory.delete', name='categorydelete'),

     

     #url(r'^pub/add/$', ArticleView, name='add'),
    # url(r'^UUBlog/', include('UUBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/', include('polls.urls')),
    #
    #url(r'^polls/', include('polls.urls', namespace="polls")),
   
)

#handler404 = 'mysite.views.my_custom_404_view'
#handler500 = 'mysite.views.my_custom_error_view'
#handler403 = 'mysite.views.my_custom_permission_denied_view'

