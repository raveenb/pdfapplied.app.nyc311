# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ThreeOneOneData'
        db.create_table('webapp_threeoneonedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('json_data', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
        ))
        db.send_create_signal('webapp', ['ThreeOneOneData'])

        # Adding model 'CommunityName'
        db.create_table('webapp_communityname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('webapp', ['CommunityName'])


    def backwards(self, orm):
        # Deleting model 'ThreeOneOneData'
        db.delete_table('webapp_threeoneonedata')

        # Deleting model 'CommunityName'
        db.delete_table('webapp_communityname')


    models = {
        'webapp.communityname': {
            'Meta': {'object_name': 'CommunityName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'webapp.threeoneonedata': {
            'Meta': {'object_name': 'ThreeOneOneData'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_data': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['webapp']