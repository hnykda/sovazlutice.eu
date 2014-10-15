# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Relic.place'
        db.alter_column('relic_relic', 'place', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.CharField')(default='', max_length=20))
        # Removing index on 'Relic', fields ['date_of_build']
        db.delete_index('relic_relic', ['date_of_build'])


        # Changing field 'Relic.gps'
        db.alter_column('relic_relic', 'gps', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.CharField')(default='', max_length=20))
        # Removing index on 'Relic', fields ['date_of_rec']
        db.delete_index('relic_relic', ['date_of_rec'])


    def backwards(self, orm):
        # Adding index on 'Relic', fields ['date_of_rec']
        db.create_index('relic_relic', ['date_of_rec'])

        # Adding index on 'Relic', fields ['date_of_build']
        db.create_index('relic_relic', ['date_of_build'])


        # Changing field 'Relic.place'
        db.alter_column('relic_relic', 'place', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Relic.date_of_build'
        db.alter_column('relic_relic', 'date_of_build', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Relic.gps'
        db.alter_column('relic_relic', 'gps', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Relic.date_of_rec'
        db.alter_column('relic_relic', 'date_of_rec', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'date_of_rec': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'gps': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'katalog_numb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'owner': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True', 'null': 'True'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']