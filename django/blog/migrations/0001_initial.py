# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Nadpis článku', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Neměnit!', unique=True, max_length=100)),
                ('body', models.TextField(verbose_name='Obsah článku')),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('pic', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, verbose_name='Titulní foto', null=True)),
                ('pic2', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_2', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic3', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_3', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic4', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_4', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic5', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_5', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic6', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_6', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic7', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_7', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
                ('pic8', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, blank=True, null=True)),
                ('picd_8', models.CharField(blank=True, verbose_name='Popis', null=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
