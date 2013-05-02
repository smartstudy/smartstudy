# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crew'
        db.create_table(u'crew_crew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'crew', ['Crew'])


    def backwards(self, orm):
        # Deleting model 'Crew'
        db.delete_table(u'crew_crew')


    models = {
        u'crew.crew': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Crew'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['crew']