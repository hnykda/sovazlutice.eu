# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.test_body'
        db.delete_column('relic_relic', 'test_body')

        # Adding field 'Relic.source_of_finance'
        db.add_column('relic_relic', 'source_of_finance',
                      self.gf('django.db.models.fields.CharField')(unique=True, default=123, max_length=30),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Relic.test_body'
        raise RuntimeError("Cannot reverse this migration. 'Relic.test_body' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Relic.test_body'
        db.add_column('relic_relic', 'test_body',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Deleting field 'Relic.source_of_finance'
        db.delete_column('relic_relic', 'source_of_finance')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'place': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sign': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['relic']