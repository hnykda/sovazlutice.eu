# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Way'
        db.create_table('ways_way', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('marks', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('interests', self.gf('django.db.models.fields.TextField')()),
            ('map_of_way', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic6', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic7', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pic8', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('ways', ['Way'])


    def backwards(self, orm):
        # Deleting model 'Way'
        db.delete_table('ways_way')


    models = {
        'ways.way': {
            'Meta': {'object_name': 'Way'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {}),
            'length': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'marks': ('django.db.models.fields.TextField', [], {}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']