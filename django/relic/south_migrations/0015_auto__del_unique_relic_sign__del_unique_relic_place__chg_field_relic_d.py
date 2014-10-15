# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Relic', fields ['gps']
        db.delete_unique('relic_relic', ['gps'])

        # Removing unique constraint on 'Relic', fields ['owner']
        db.delete_unique('relic_relic', ['owner'])

        # Removing unique constraint on 'Relic', fields ['source_of_finance']
        db.delete_unique('relic_relic', ['source_of_finance'])

        # Removing unique constraint on 'Relic', fields ['place']
        db.delete_unique('relic_relic', ['place'])

        # Removing unique constraint on 'Relic', fields ['sign']
        db.delete_unique('relic_relic', ['sign'])


        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Adding unique constraint on 'Relic', fields ['sign']
        db.create_unique('relic_relic', ['sign'])

        # Adding unique constraint on 'Relic', fields ['place']
        db.create_unique('relic_relic', ['place'])


        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=None))
        # Adding unique constraint on 'Relic', fields ['source_of_finance']
        db.create_unique('relic_relic', ['source_of_finance'])

        # Adding unique constraint on 'Relic', fields ['owner']
        db.create_unique('relic_relic', ['owner'])

        # Adding unique constraint on 'Relic', fields ['gps']
        db.create_unique('relic_relic', ['gps'])


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '8'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']