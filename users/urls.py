from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<user_id>\d+)/$', views.detail)
)