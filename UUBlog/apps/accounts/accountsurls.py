#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

from UUBlog import settings
from UUBlog.apps.accounts.views import baseaccountsview, viewaccounts
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('',
)

#帐户信息
urlpatterns += patterns('',
    url(r'^accounts/login/$', viewaccounts.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', viewaccounts.LogoutView.as_view(), name='logout'),
    url(r'^accounts/register/$', viewaccounts.RegisterView.as_view(), name='register'),
     
    url(r'^(?P<uid>\d+)/accounts/$', viewaccounts.BaseView.as_view(), name='accountsbase'),
    url(r'^(?P<uid>\d+)/accounts/avatar/$', viewaccounts.AvatarView.as_view(), name='accountsavatar'),
    url(r'^(?P<uid>\d+)/accounts/contact/$', viewaccounts.ContactView.as_view(), name='accountscontact'),
    url(r'^(?P<uid>\d+)/accounts/info/$', viewaccounts.InfoView.as_view(), name='accountsinfo'),
    url(r'^(?P<uid>\d+)/accounts/security/$', viewaccounts.SecurityView.as_view(), name='accountssecurity'),
     
)

