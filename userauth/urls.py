from django.conf.urls import patterns, include, url

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'userauth/login.html'},
        name='userauth_login'),
    url(r'^logout/$', 'logout', {'next_page': 'home/'},
        name='userauth_logout'),
    url(r'^password-change/$', 'password_change',
        {'template_name': 'userauth/password_change_form.html'},
        name='userauth_password_change'),
    url(r'^password_change_done/$', 'password_change_done',
        {'template_name': 'userauth/password_change_done.html'},
        name='userauth_password_change_done')
)