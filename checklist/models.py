from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta



class Site(models.Model):
	name = models.CharField(max_length=100, default="",blank=True)
	location = models.ForeignKey('Location')
	
	def __unicode__(self):
		return self.name

class Location(models.Model):
	address = models.CharField(max_length=300)
	city = models.CharField(max_length=50)
	postalCode = models.CharField(max_length=7)
	province = models.CharField(max_length=40)
	
	def __unicode__(self):
		return u"%s, %s" % (self.address, self.city)

class Task(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name

class Checklist(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	fileNumber = models.IntegerField('File Number')
	landDistrictType = models.CharField(max_length=300)  #... they have not provided a description of this field yet...
	site = models.ForeignKey(Site)
	tasks = models.ManyToManyField(Task, through='ChecklistItem')
	created_date = models.DateTimeField('created date', auto_now_add=True)
	due_date = models.DateTimeField('due date', blank=True)
	
	def __unicode__(self):
		return self.title	
	
class ChecklistItem(models.Model):
	checklist = models.ForeignKey(Checklist)
	task = models.ForeignKey(Task)
	
	checked = models.BooleanField(default=False)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return u"%s : %s" % (self.checklist.title, self.task.name)

class Assignment(models.Model):
	surveyor = models.ForeignKey(User, related_name='assigned_to')
	checklist = models.ForeignKey(Checklist)
	manager = models.ForeignKey(User, related_name='assigned_by')
	date = models.DateField() 
	
	def __unicode__(self):
		return u"%s : %s" % (self.surveyor.last_name, self.checklist.title)
