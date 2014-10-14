from django.conf.urls import patterns, url
from ways import views

urlpatterns = patterns('',

url(r'^$', views.ways_index, name='index'),

url(r'^view/(?P<slug>[^\.]+)', 
    views.view_way, 
    name='view_way'),
)
