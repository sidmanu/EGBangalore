from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EGBangalore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'estore.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^estore/', include('estore.urls', namespace='estore')),

)
