# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import Context,RequestContext
from models import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from httplib2 import Http
from urllib import urlencode

from xml.etree import ElementTree 


@login_required
def dashboard(request):
	return render_to_response('checklist/dashboard.html', {'user': request.user})

@login_required
def inbox(request):
	#assignments = get_object_or_404(Assignment, surveyor=request.user)
	assignments = Assignment.objects.filter(surveyor=request.user)
	return render_to_response('checklist/inbox.html', {'assignments' : assignments, 'user': request.user})

@login_required
def showAssignment(request, assignmentID):
	assignment = get_object_or_404(Assignment, pk=assignmentID)
	manager = assignment.manager
	surveyor = assignment.surveyor
	checklist = assignment.checklist
	date = assignment.date
	
	
	# Static Google Maps API url example
	# http://maps.google.com/maps/api/staticmap?center=1619+Kenmore+Rd,Victoria,BC&zoom=14&size=512x512&maptype=roadmap&sensor=false&markers=color:blue|label:Site|1619+Kenmore+Rd,Victoria,BC
	location = checklist.site.location	
	location_slug = "%s,%s,%s" % (slugify(location.address),
	 									slugify(location.city), 
										slugify(location.province))
	map_width = '640'
	map_height = '640'
	map_url = "http://maps.google.com/maps/api/staticmap" + \
			"?center=%s&zoom=14&size=%sx%s&maptype=roadmap&sensor=false&markers=color:blue|label:S|%s" \
			% (location_slug, map_width, map_height, location_slug)
			
	weather_url = "http://www.google.com/ig/api?weather=%s" % location_slug
	print weather_url
	
	# we probably want to put weather stuff somewhere else since it can be slow to load
	# ie. have a "get weather" link
	
	h = Http()
	response, content = h.request(weather_url, "GET")
	el = ElementTree.XML(content)
	current = el.find("weather/current_conditions")
	currentDict = dict()
	for sub in current:
		currentDict[sub.tag] = sub.attrib['data']
	
	
	# We need to decide whether assignments have due dates, or checklists, or both
	# Also, should assignments indicate checklistItems to be covered (allowing for 
	# multiple surveyors to work on the same checklist via their seperate assignments)?
	
	return render_to_response('checklist/assignment.html',
	 	{'assignment' : assignment, 'manager' : manager, 'surveyor': surveyor, 'checklist' : checklist, 'due_date' : date,
	 		'map_url':map_url, 'location':location, 'currentWeather' : currentDict})

@login_required
def showChecklist(request, assignmentID, checklistID):
	checklist = get_object_or_404(Checklist, pk=checklistID)
	assignment = get_object_or_404(Assignment, pk=assignmentID)
	tasks = checklist.tasks.all()
	if assignment.checklist != checklist or assignment.surveyor != request.user:
		Http404()
			
	return render_to_response("checklist/checklist.html",
	 {'assignment':assignment,'checklist':checklist, 'tasks':tasks}, context_instance=RequestContext(request))

@login_required
def submitChecklist(request):
	if request.method == 'POST':
		assignment_id = request.POST['assignment']
		checklist_id = request.POST['checklist']
		assignment = Assignment.objects.get(pk=assignment_id)
		checklist = Checklist.objects.get(pk=checklist_id)
		
		assignment.submitted = True
		assignment.save()
		
		# here is where we'll have logic to check if all assignments for a 
		# particular checklist are completed (support for multiple surveyors
		# on one checklist).  For now just say the full checklist is complete
		checklist.completed = True
		checklist.save()
		
		return render_to_response('checklist/dashboard.html',
		 {'user': request.user, 'status_message':'Assignment Submitted'})
	else:
		return render_to_response('checklist/dashboard.html',
		 {'user': request.user, 'error_message':'Invalid Assignment Submission'})

@login_required
def surveyorInbox(request):
	pass