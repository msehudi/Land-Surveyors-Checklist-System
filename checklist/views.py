# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import Context,RequestContext
from models import *
from django.shortcuts import render_to_response, get_object_or_404


	