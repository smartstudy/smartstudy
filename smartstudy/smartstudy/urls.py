# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import smartstudy.views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', smartstudy.views.HomeView.as_view(), name='home'),
    url(r'^privacy', smartstudy.views.privacy, name='privacy'),
    # url(r'^smartstudy/', include('smartstudy.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
