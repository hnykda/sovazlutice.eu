# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.pic'
        db.add_column('blog_blog', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(blank=True, default=2, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.pic'
        db.delete_column('blog_blog', 'pic')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']