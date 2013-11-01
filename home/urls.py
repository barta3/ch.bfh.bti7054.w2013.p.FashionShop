from django.conf.urls import patterns, url

from home import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<cat_name>\w+)/$', views.productListByCategory),
    url(r'^(?P<cat_name>\w+)/(?P<prod_id>\w+)/$' , views.productDetail),
)