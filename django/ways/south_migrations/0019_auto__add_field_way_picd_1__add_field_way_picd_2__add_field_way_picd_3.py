# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Way', fields ['length']
        db.delete_unique('ways_way', ['length'])

        # Adding field 'Way.picd_1'
        db.add_column('ways_way', 'picd_1',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_2'
        db.add_column('ways_way', 'picd_2',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_3'
        db.add_column('ways_way', 'picd_3',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_4'
        db.add_column('ways_way', 'picd_4',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_5'
        db.add_column('ways_way', 'picd_5',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_6'
        db.add_column('ways_way', 'picd_6',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_7'
        db.add_column('ways_way', 'picd_7',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Way.picd_8'
        db.add_column('ways_way', 'picd_8',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Way.picd_1'
        db.delete_column('ways_way', 'picd_1')

        # Deleting field 'Way.picd_2'
        db.delete_column('ways_way', 'picd_2')

        # Deleting field 'Way.picd_3'
        db.delete_column('ways_way', 'picd_3')

        # Deleting field 'Way.picd_4'
        db.delete_column('ways_way', 'picd_4')

        # Deleting field 'Way.picd_5'
        db.delete_column('ways_way', 'picd_5')

        # Deleting field 'Way.picd_6'
        db.delete_column('ways_way', 'picd_6')

        # Deleting field 'Way.picd_7'
        db.delete_column('ways_way', 'picd_7')

        # Deleting field 'Way.picd_8'
        db.delete_column('ways_way', 'picd_8')

        # Adding unique constraint on 'Way', fields ['length']
        db.create_unique('ways_way', ['length'])


    models = {
        'ways.way': {
            'Meta': {'object_name': 'Way'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest1_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest1_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interest2_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest2_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interest3_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interest3_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'map_of_way': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'marks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_4': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_5': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_6': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_7': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picd_8': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'the_path': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']