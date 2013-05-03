# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Crew.name'
        db.add_column(u'crew_crew', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crew.email'
        db.add_column(u'crew_crew', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crew.homepage'
        db.add_column(u'crew_crew', 'homepage',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crew.facebook'
        db.add_column(u'crew_crew', 'facebook',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crew.twitter'
        db.add_column(u'crew_crew', 'twitter',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Crew.name'
        db.delete_column(u'crew_crew', 'name')

        # Deleting field 'Crew.email'
        db.delete_column(u'crew_crew', 'email')

        # Deleting field 'Crew.homepage'
        db.delete_column(u'crew_crew', 'homepage')

        # Deleting field 'Crew.facebook'
        db.delete_column(u'crew_crew', 'facebook')

        # Deleting field 'Crew.twitter'
        db.delete_column(u'crew_crew', 'twitter')


    models = {
        u'crew.crew': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Crew'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['crew']