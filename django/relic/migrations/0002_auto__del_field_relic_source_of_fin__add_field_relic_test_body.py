# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.source_of_fin'
        db.delete_column('relic_relic', 'source_of_fin')

        # Adding field 'Relic.test_body'
        db.add_column('relic_relic', 'test_body',
                      self.gf('django.db.models.fields.TextField')(default='aga'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Relic.source_of_fin'
        raise RuntimeError("Cannot reverse this migration. 'Relic.source_of_fin' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Relic.source_of_fin'
        db.add_column('relic_relic', 'source_of_fin',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=30),
                      keep_default=False)

        # Deleting field 'Relic.test_body'
        db.delete_column('relic_relic', 'test_body')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'test_body': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        }
    }

    complete_apps = ['relic']