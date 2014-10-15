# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.CharField')(null=True, max_length=20))

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.CharField')(null=True, max_length=20))

        # Changing field 'Relic.price_of_rec'
        db.alter_column('relic_relic', 'price_of_rec', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Relic.price_of_rec'
        db.alter_column('relic_relic', 'price_of_rec', self.gf('django.db.models.fields.IntegerField')(default=None))

    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'date_of_rec': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'katalog_numb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '8', 'blank': 'True'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']