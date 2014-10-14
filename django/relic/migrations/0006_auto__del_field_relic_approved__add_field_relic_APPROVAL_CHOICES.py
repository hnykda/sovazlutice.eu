# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.approved'
        db.delete_column('relic_relic', 'approved')

        # Adding field 'Relic.APPROVAL_CHOICES'
        db.add_column('relic_relic', 'APPROVAL_CHOICES',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Relic.approved'
        raise RuntimeError("Cannot reverse this migration. 'Relic.approved' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Relic.approved'
        db.add_column('relic_relic', 'approved',
                      self.gf('django.db.models.fields.CharField')(max_length=1),
                      keep_default=False)

        # Deleting field 'Relic.APPROVAL_CHOICES'
        db.delete_column('relic_relic', 'APPROVAL_CHOICES')


    models = {
        'relic.relic': {
            'APPROVAL_CHOICES': ('django.db.models.fields.BooleanField', [], {}),
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sign': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['relic']