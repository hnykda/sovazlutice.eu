from django.conf.urls import patterns, url
from relic import views

urlpatterns = patterns('',

url(r'^$', views.relics_index, name='index'),

url(r'^view/(?P<slug>[^\.]+)', 
    views.view_relic, 
    name='view_relic'),
)
