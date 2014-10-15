# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relic'
        db.create_table('relic_relic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True)),
            ('posted', self.gf('django.db.models.fields.DateField')(db_index=True, auto_now_add=True, blank=True)),
            ('type_of', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('gps', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('date_of_build', self.gf('django.db.models.fields.DateField')(db_index=True, auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('date_of_rec', self.gf('django.db.models.fields.DateField')(db_index=True, auto_now_add=True, blank=True)),
            ('price_of_rec', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('source_of_fin', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('sign', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('relic', ['Relic'])


    def backwards(self, orm):
        # Deleting model 'Relic'
        db.delete_table('relic_relic')


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_rec': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'price_of_rec': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source_of_fin': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'type_of': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        }
    }

    complete_apps = ['relic']