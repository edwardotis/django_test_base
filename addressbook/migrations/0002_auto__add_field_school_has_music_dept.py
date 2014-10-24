# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'School.has_music_dept'
        db.add_column('addressbook_school', 'has_music_dept',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.has_music_dept'
        db.delete_column('addressbook_school', 'has_music_dept')


    models = {
        u'addressbook.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'has_music_dept': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'school_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['addressbook']