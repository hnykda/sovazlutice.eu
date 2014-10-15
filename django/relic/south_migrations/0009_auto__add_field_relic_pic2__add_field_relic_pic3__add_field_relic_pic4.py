# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Relic.pic2'
        db.add_column('relic_relic', 'pic2',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic3'
        db.add_column('relic_relic', 'pic3',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic4'
        db.add_column('relic_relic', 'pic4',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic5'
        db.add_column('relic_relic', 'pic5',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic6'
        db.add_column('relic_relic', 'pic6',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic7'
        db.add_column('relic_relic', 'pic7',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Adding field 'Relic.pic8'
        db.add_column('relic_relic', 'pic8',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)


        # Changing field 'Relic.pic'
        db.alter_column('relic_relic', 'pic', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

    def backwards(self, orm):
        # Deleting field 'Relic.pic2'
        db.delete_column('relic_relic', 'pic2')

        # Deleting field 'Relic.pic3'
        db.delete_column('relic_relic', 'pic3')

        # Deleting field 'Relic.pic4'
        db.delete_column('relic_relic', 'pic4')

        # Deleting field 'Relic.pic5'
        db.delete_column('relic_relic', 'pic5')

        # Deleting field 'Relic.pic6'
        db.delete_column('relic_relic', 'pic6')

        # Deleting field 'Relic.pic7'
        db.delete_column('relic_relic', 'pic7')

        # Deleting field 'Relic.pic8'
        db.delete_column('relic_relic', 'pic8')


        # Changing field 'Relic.pic'
        db.alter_column('relic_relic', 'pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, default=1))

    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
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