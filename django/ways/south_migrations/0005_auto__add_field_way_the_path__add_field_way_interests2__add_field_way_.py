# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Way.the_path'
        db.add_column('ways_way', 'the_path',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Adding field 'Way.interests2'
        db.add_column('ways_way', 'interests2',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Way.interests3'
        db.add_column('ways_way', 'interests3',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)


        # Changing field 'Way.marks'
        db.alter_column('ways_way', 'marks', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Way.pic2'
        db.alter_column('ways_way', 'pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic3'
        db.alter_column('ways_way', 'pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic4'
        db.alter_column('ways_way', 'pic4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic5'
        db.alter_column('ways_way', 'pic5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic6'
        db.alter_column('ways_way', 'pic6', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic1'
        db.alter_column('ways_way', 'pic1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic8'
        db.alter_column('ways_way', 'pic8', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.pic7'
        db.alter_column('ways_way', 'pic7', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Way.interests'
        db.alter_column('ways_way', 'interests', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Way.the_path'
        db.delete_column('ways_way', 'the_path')

        # Deleting field 'Way.interests2'
        db.delete_column('ways_way', 'interests2')

        # Deleting field 'Way.interests3'
        db.delete_column('ways_way', 'interests3')


        # Changing field 'Way.marks'
        db.alter_column('ways_way', 'marks', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Way.pic2'
        db.alter_column('ways_way', 'pic2', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic3'
        db.alter_column('ways_way', 'pic3', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic4'
        db.alter_column('ways_way', 'pic4', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic5'
        db.alter_column('ways_way', 'pic5', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic6'
        db.alter_column('ways_way', 'pic6', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic1'
        db.alter_column('ways_way', 'pic1', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic8'
        db.alter_column('ways_way', 'pic8', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.pic7'
        db.alter_column('ways_way', 'pic7', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Way.interests'
        db.alter_column('ways_way', 'interests', self.gf('django.db.models.fields.TextField')(default=None))

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
            'the_path': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ways']