from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^relic/', include('relic.urls', namespace="relics")),
    url(r'^ways/', include('ways.urls', namespace="ways")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)
