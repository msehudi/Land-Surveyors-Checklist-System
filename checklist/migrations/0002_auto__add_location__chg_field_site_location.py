# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('checklist_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('checklist', ['Location'])

        # Renaming column for 'Site.location' to match new field type.
        db.rename_column('checklist_site', 'location', 'location_id')
        # Changing field 'Site.location'
        db.alter_column('checklist_site', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['checklist.Location']))

        # Adding index on 'Site', fields ['location']
        db.create_index('checklist_site', ['location_id'])


    def backwards(self, orm):
        
        # Removing index on 'Site', fields ['location']
        db.delete_index('checklist_site', ['location_id'])

        # Deleting model 'Location'
        db.delete_table('checklist_location')

        # Renaming column for 'Site.location' to match new field type.
        db.rename_column('checklist_site', 'location_id', 'location')
        # Changing field 'Site.location'
        db.alter_column('checklist_site', 'location', self.gf('django.db.models.fields.CharField')(max_length=300))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'checklist.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Checklist']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigned_by'", 'to': "orm['auth.User']"}),
            'surveyor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigned_to'", 'to': "orm['auth.User']"})
        },
        'checklist.checklist': {
            'Meta': {'object_name': 'Checklist'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fileNumber': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landDistrictType': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Site']"}),
            'tasks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['checklist.Task']", 'through': "orm['checklist.ChecklistItem']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'checklist.checklistitem': {
            'Meta': {'object_name': 'ChecklistItem'},
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Checklist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Task']"})
        },
        'checklist.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'checklist.site': {
            'Meta': {'object_name': 'Site'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Location']"})
        },
        'checklist.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['checklist']
