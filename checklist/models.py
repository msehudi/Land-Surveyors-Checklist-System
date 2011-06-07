from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Site(models.Model):
	location = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.location

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
	created_date = models.DateTimeField('created date')
	tasks = models.ManyToManyField(Task, through='ChecklistItem')
	due_date = models.DateTimeField('due date')
	
	def __unicode__(self):
		return self.title	

		
class ChecklistItem(models.Model):
	checklist = models.ForeignKey(Checklist)
	task = models.ForeignKey(Task)
	checked = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.checklist.title + ' : '+self.task.name
	

	 	
class Assignment(models.Model):
	surveyor = models.ForeignKey(User, related_name='assigned_to')
	checklist = models.ForeignKey(Checklist)
	manager = models.ForeignKey(User, related_name='assigned_by')
	date = models.DateField() 
	
	def __unicode__(self):
		return self.surveyor.last_name +' : '+self.checklist.title

