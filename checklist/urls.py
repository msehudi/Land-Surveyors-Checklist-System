from django.conf.urls.defaults import patterns, include, url
from views import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
)