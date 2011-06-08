from django.conf.urls.defaults import patterns, include, url
from views import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^dashboard', dashboard, name='dashboard'),
	url(r'^inbox', inbox, name='inbox'),
	#url(r'^assignment', showAssignment, name='assignment'),
	url(r'^assignment/(?P<assignmentID>\d+)/$', showAssignment, name='assignment'),
	url(r'^assignment/(?P<assignmentID>\d+)/checklist/(?P<checklistID>\d+)/$', showChecklist, name='checklist'),
)