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
            ('marks', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('the_path', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('length', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('interest1_name', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('interest1_body', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('interest2_name', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('interest2_body', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('interest3_name', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('interest3_body', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('map_of_way', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic6', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic7', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('pic8', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
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
            'interest1_body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interest1_name': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interest2_body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interest2_name': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interest3_body': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interest3_name': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'length': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'marks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'the_path': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']