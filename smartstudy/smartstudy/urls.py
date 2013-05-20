# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from smartstudy.settings.base import MEDIA_ROOT
import smartstudy.views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', smartstudy.views.HomeView.as_view(), name='home'),
    url(r'^privacy', TemplateView.as_view(template_name="privacy.html")),
    # url(r'^smartstudy/', include('smartstudy.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
