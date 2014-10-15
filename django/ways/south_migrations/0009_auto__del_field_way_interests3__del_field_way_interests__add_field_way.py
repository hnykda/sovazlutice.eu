# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Way.interests3'
        db.delete_column('ways_way', 'interests3')

        # Deleting field 'Way.interests'
        db.delete_column('ways_way', 'interests')

        # Adding field 'Way.the_path'
        db.add_column('ways_way', 'the_path',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest1_name'
        db.add_column('ways_way', 'interest1_name',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest1_body'
        db.add_column('ways_way', 'interest1_body',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest2_name'
        db.add_column('ways_way', 'interest2_name',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest2_body'
        db.add_column('ways_way', 'interest2_body',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest3_name'
        db.add_column('ways_way', 'interest3_name',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interest3_body'
        db.add_column('ways_way', 'interest3_body',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Way.map_of_way'
        db.alter_column('ways_way', 'map_of_way', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

    def backwards(self, orm):
        # Adding field 'Way.interests3'
        db.add_column('ways_way', 'interests3',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.interests'
        db.add_column('ways_way', 'interests',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

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


        # Changing field 'Way.map_of_way'
        db.alter_column('ways_way', 'map_of_way', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

    models = {
        'ways.way': {
            'Meta': {'object_name': 'Way'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest1_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest1_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest2_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest2_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest3_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest3_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'marks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'the_path': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']