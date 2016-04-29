# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import ways.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('body', models.TextField(verbose_name='Popis stezky obecně')),
                ('marks', models.CharField(max_length=100, verbose_name='Značka')),
                ('the_path', models.TextField(verbose_name='Popis trasy', null=True, blank=True)),
                ('length', models.SlugField(max_length=100, verbose_name='Délka')),
                ('interest1_name', models.CharField(max_length=100, verbose_name='Název zajímavosti 1', blank=True, null=True)),
                ('interest1_body', models.TextField(verbose_name='Popis zajímavosti 1', null=True, blank=True)),
                ('interest2_name', models.CharField(max_length=100, verbose_name='Název zajímavosti 2', blank=True, null=True)),
                ('interest2_body', models.TextField(verbose_name='Popis zajímavosti 2', null=True, blank=True)),
                ('interest3_name', models.CharField(max_length=100, verbose_name='Název zajímavosti 3', blank=True, null=True)),
                ('interest3_body', models.TextField(verbose_name='Popis zajímavosti 3', null=True, blank=True)),
                ('map_of_way', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to='pictures/ways/maps')),
                ('pic1', easy_thumbnails.fields.ThumbnailerImageField(upload_to=ways.models.get_name_file, verbose_name='Titulní foto', blank=True, null=True)),
                ('picd_1', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic2', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_2', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic3', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_3', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic4', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_4', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic5', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_5', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic6', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_6', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic7', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_7', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
                ('pic8', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=ways.models.get_name_file)),
                ('picd_8', models.CharField(max_length=100, verbose_name='Popis', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
