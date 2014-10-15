# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.test'
        db.delete_column('relic_relic', 'test')

        # Adding field 'Relic.test1'
        db.add_column('relic_relic', 'test1',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, db_index=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Relic.test'
        raise RuntimeError("Cannot reverse this migration. 'Relic.test' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Relic.test'
        db.add_column('relic_relic', 'test',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, db_index=True, blank=True),
                      keep_default=False)

        # Deleting field 'Relic.test1'
        db.delete_column('relic_relic', 'test1')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {}),
            'sign': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'test1': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']