# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.picd_1'
        db.add_column('blog_blog', 'picd_1',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic2'
        db.add_column('blog_blog', 'pic2',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_2'
        db.add_column('blog_blog', 'picd_2',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic3'
        db.add_column('blog_blog', 'pic3',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_3'
        db.add_column('blog_blog', 'picd_3',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic4'
        db.add_column('blog_blog', 'pic4',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_4'
        db.add_column('blog_blog', 'picd_4',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic5'
        db.add_column('blog_blog', 'pic5',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_5'
        db.add_column('blog_blog', 'picd_5',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic6'
        db.add_column('blog_blog', 'pic6',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_6'
        db.add_column('blog_blog', 'picd_6',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic7'
        db.add_column('blog_blog', 'pic7',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_7'
        db.add_column('blog_blog', 'picd_7',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.pic8'
        db.add_column('blog_blog', 'pic8',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Blog.picd_8'
        db.add_column('blog_blog', 'picd_8',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)


        # Changing field 'Blog.pic'
        db.alter_column('blog_blog', 'pic', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

    def backwards(self, orm):
        # Deleting field 'Blog.picd_1'
        db.delete_column('blog_blog', 'picd_1')

        # Deleting field 'Blog.pic2'
        db.delete_column('blog_blog', 'pic2')

        # Deleting field 'Blog.picd_2'
        db.delete_column('blog_blog', 'picd_2')

        # Deleting field 'Blog.pic3'
        db.delete_column('blog_blog', 'pic3')

        # Deleting field 'Blog.picd_3'
        db.delete_column('blog_blog', 'picd_3')

        # Deleting field 'Blog.pic4'
        db.delete_column('blog_blog', 'pic4')

        # Deleting field 'Blog.picd_4'
        db.delete_column('blog_blog', 'picd_4')

        # Deleting field 'Blog.pic5'
        db.delete_column('blog_blog', 'pic5')

        # Deleting field 'Blog.picd_5'
        db.delete_column('blog_blog', 'picd_5')

        # Deleting field 'Blog.pic6'
        db.delete_column('blog_blog', 'pic6')

        # Deleting field 'Blog.picd_6'
        db.delete_column('blog_blog', 'picd_6')

        # Deleting field 'Blog.pic7'
        db.delete_column('blog_blog', 'pic7')

        # Deleting field 'Blog.picd_7'
        db.delete_column('blog_blog', 'picd_7')

        # Deleting field 'Blog.pic8'
        db.delete_column('blog_blog', 'pic8')

        # Deleting field 'Blog.picd_8'
        db.delete_column('blog_blog', 'picd_8')


        # Changing field 'Blog.pic'
        db.alter_column('blog_blog', 'pic', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic5': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic6': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic7': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'pic8': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_1': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_2': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_3': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_4': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_5': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_6': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_7': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'picd_8': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']