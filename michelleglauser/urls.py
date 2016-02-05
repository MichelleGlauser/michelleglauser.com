# coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'michelleglauser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mg_app.views.index', name='home'),
    url(r'^techtonic/', 'mg_app.views.techtonic', name='techtonic'),
)
