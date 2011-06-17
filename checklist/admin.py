from checklist.models import *
from django.contrib import admin

class ItemInline(admin.StackedInline):
	model = ChecklistItem
	extra = 0

class ChecklistAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,    {'fields' : ['title','fileNumber','description','site']}),
		('Dates', {'fields' : [ 'due_date']})
	]
	inlines = [ItemInline]
	
	list_display = ('title', 'created_date', 'due_date')
	list_filter = ['created_date', 'due_date']
	search_fields = ['title', 'description', 'location']

class AssignmentAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ('surveyor','checklist', 'status','approved')}),
	]

admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Task)
admin.site.register(Site)
admin.site.register(Assignment)
admin.site.register(Location)
