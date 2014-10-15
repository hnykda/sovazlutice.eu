# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Way.the_path'
        db.delete_column('ways_way', 'the_path')


    def backwards(self, orm):
        # Adding field 'Way.the_path'
        db.add_column('ways_way', 'the_path',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    models = {
        'ways.way': {
            'Meta': {'object_name': 'Way'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interests2': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'interests3': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'length': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'marks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']