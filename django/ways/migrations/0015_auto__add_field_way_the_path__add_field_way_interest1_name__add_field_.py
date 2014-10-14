# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Way.the_path'
        db.add_column('ways_way', 'the_path',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest1_name'
        db.add_column('ways_way', 'interest1_name',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest1_body'
        db.add_column('ways_way', 'interest1_body',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest2_name'
        db.add_column('ways_way', 'interest2_name',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest2_body'
        db.add_column('ways_way', 'interest2_body',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest3_name'
        db.add_column('ways_way', 'interest3_name',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interest3_body'
        db.add_column('ways_way', 'interest3_body',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Way.the_path'
        db.delete_column('ways_way', 'the_path')

        # Deleting field 'Way.interest1_name'
        db.delete_column('ways_way', 'interest1_name')

        # Deleting field 'Way.interest1_body'
        db.delete_column('ways_way', 'interest1_body')

        # Deleting field 'Way.interest2_name'
        db.delete_column('ways_way', 'interest2_name')

        # Deleting field 'Way.interest2_body'
        db.delete_column('ways_way', 'interest2_body')

        # Deleting field 'Way.interest3_name'
        db.delete_column('ways_way', 'interest3_name')

        # Deleting field 'Way.interest3_body'
        db.delete_column('ways_way', 'interest3_body')


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
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
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
            'the_path': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']