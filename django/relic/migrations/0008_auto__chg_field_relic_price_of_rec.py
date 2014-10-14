# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Relic.price_of_rec'
        db.alter_column('relic_relic', 'price_of_rec', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Relic.price_of_rec'
        db.alter_column('relic_relic', 'price_of_rec', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {}),
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