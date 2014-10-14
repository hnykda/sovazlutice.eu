# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Relic.test'
        db.add_column('relic_relic', 'test',
                      self.gf('django.db.models.fields.DateField')(null=True, auto_now_add=True, blank=True, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Relic.test'
        db.delete_column('relic_relic', 'test')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {}),
            'sign': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'test': ('django.db.models.fields.DateField', [], {'null': 'True', 'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']