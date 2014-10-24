# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('addressbook_school', (
            ('school_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'addressbook', ['School'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('school')


    models = {
        u'addressbook.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'school_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['addressbook']