# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relic.pic_n'
        db.delete_column('relic_relic', 'pic_n')


    def backwards(self, orm):
        # Adding field 'Relic.pic_n'
        db.add_column('relic_relic', 'pic_n',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True),
                      keep_default=False)


    models = {
        'relic.relic': {
            'Meta': {'object_name': 'Relic'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_of_build': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'katalog_numb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'price_of_rec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reconstruction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source_of_finance': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type_of_r': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'w_czp': ('django.db.models.fields.BooleanField', [], {}),
            'w_kc': ('django.db.models.fields.BooleanField', [], {}),
            'w_ssr': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['relic']