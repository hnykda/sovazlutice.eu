# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.APPROVAL_CHOICES'
        db.delete_column('relic_relic', 'APPROVAL_CHOICES')

        # Adding field 'Relic.w_ssr'
        db.add_column('relic_relic', 'w_ssr',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Relic.w_kc'
        db.add_column('relic_relic', 'w_kc',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Relic.w_czp'
        db.add_column('relic_relic', 'w_czp',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Relic.APPROVAL_CHOICES'
        raise RuntimeError("Cannot reverse this migration. 'Relic.APPROVAL_CHOICES' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Relic.APPROVAL_CHOICES'
        db.add_column('relic_relic', 'APPROVAL_CHOICES',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)

        # Deleting field 'Relic.w_ssr'
        db.delete_column('relic_relic', 'w_ssr')

        # Deleting field 'Relic.w_kc'
        db.delete_column('relic_relic', 'w_kc')

        # Deleting field 'Relic.w_czp'
        db.delete_column('relic_relic', 'w_czp')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']