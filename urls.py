# coding:utf8
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import issues.controllers
from djangox.route import discover_controllers

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', issue.controllers.index),
    url(r'', include('social_auth.urls')),
    (r'', discover_controllers(issues.controllers)),
    # Examples:
    # url(r'^$', 'issuetrackr.views.home', name='home'),
    # url(r'^issuetrackr/', include('issuetrackr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
