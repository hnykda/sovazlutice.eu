# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Relic.pic'
        db.add_column('relic_relic', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Relic.pic'
        db.delete_column('relic_relic', 'pic')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        }
    }

    complete_apps = ['relic']