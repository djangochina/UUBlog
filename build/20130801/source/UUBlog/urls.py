#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

import settings
from django.contrib import admin
from UUBlog.apps.blog import blogurls
from UUBlog.apps.accounts import accountsurls
admin.autodiscover()



urlpatterns = patterns('',

)


urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
     url(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns+=blogurls.urlpatterns

urlpatterns+=accountsurls.urlpatterns

