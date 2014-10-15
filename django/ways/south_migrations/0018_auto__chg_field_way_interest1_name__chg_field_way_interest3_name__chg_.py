# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Way.interest1_name'
        db.alter_column('ways_way', 'interest1_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Way.interest3_name'
        db.alter_column('ways_way', 'interest3_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Way.interest2_name'
        db.alter_column('ways_way', 'interest2_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Way.interest1_name'
        db.alter_column('ways_way', 'interest1_name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Way.interest3_name'
        db.alter_column('ways_way', 'interest3_name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Way.interest2_name'
        db.alter_column('ways_way', 'interest2_name', self.gf('django.db.models.fields.TextField')(null=True))

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
            'length': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'the_path': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        }
    }

    complete_apps = ['ways']