# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Relic.picd_2'
        db.add_column('relic_relic', 'picd_2',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_3'
        db.add_column('relic_relic', 'picd_3',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_4'
        db.add_column('relic_relic', 'picd_4',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_5'
        db.add_column('relic_relic', 'picd_5',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_6'
        db.add_column('relic_relic', 'picd_6',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_7'
        db.add_column('relic_relic', 'picd_7',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Relic.picd_8'
        db.add_column('relic_relic', 'picd_8',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Relic.picd_2'
        db.delete_column('relic_relic', 'picd_2')

        # Deleting field 'Relic.picd_3'
        db.delete_column('relic_relic', 'picd_3')

        # Deleting field 'Relic.picd_4'
        db.delete_column('relic_relic', 'picd_4')

        # Deleting field 'Relic.picd_5'
        db.delete_column('relic_relic', 'picd_5')

        # Deleting field 'Relic.picd_6'
        db.delete_column('relic_relic', 'picd_6')

        # Deleting field 'Relic.picd_7'
        db.delete_column('relic_relic', 'picd_7')

        # Deleting field 'Relic.picd_8'
        db.delete_column('relic_relic', 'picd_8')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'katalog_numb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'owner': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'picd_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'reconstruction': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '8', 'null': 'True'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']