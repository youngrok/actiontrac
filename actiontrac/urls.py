from django.conf.urls import patterns, include, url

from django.contrib import admin
from djangox.route import discover_controllers
import unilogin.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'actiontrac.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'', discover_controllers('tracker.controllers')),
    (r'', include(unilogin.urls))

)
