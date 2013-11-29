from django.conf.urls import patterns, url
from checkout import views


urlpatterns = patterns('',
    url(r'^$', views.overview),
    url(r'^confirm/$', views.confirmation),
)