# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.posted'
        db.delete_column('relic_relic', 'posted')

        # Deleting field 'Relic.type_of'
        db.delete_column('relic_relic', 'type_of')

        # Deleting field 'Relic.test'
        db.delete_column('relic_relic', 'test')

        # Adding field 'Relic.type_of_r'
        db.add_column('relic_relic', 'type_of_r',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Relic.posted'
        db.add_column('relic_relic', 'posted',
                      self.gf('django.db.models.fields.DateField')(db_index=True, auto_now_add=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'Relic.type_of'
        db.add_column('relic_relic', 'type_of',
                      self.gf('django.db.models.fields.CharField')(max_length=20, default=1, unique=True),
                      keep_default=False)

        # Adding field 'Relic.test'
        db.add_column('relic_relic', 'test',
                      self.gf('django.db.models.fields.DateField')(null=True, auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Deleting field 'Relic.type_of_r'
        db.delete_column('relic_relic', 'type_of_r')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '8'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']