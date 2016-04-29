# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import relic.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Název', max_length=100, unique=True)),
                ('place', models.CharField(verbose_name='Umístění', max_length=100, blank=True)),
                ('gps', models.CharField(verbose_name='GPS', max_length=50, blank=True)),
                ('date_of_build', models.CharField(verbose_name='Datum vzniku', max_length=20, blank=True, null=True)),
                ('reconstruction', models.CharField(verbose_name='Rekonstrukce', max_length=200, blank=True, null=True)),
                ('price_of_rec', models.IntegerField(verbose_name='Cena rekonstrukce', blank=True, null=True)),
                ('source_of_finance', models.CharField(verbose_name='Zdroj financí', max_length=30, blank=True)),
                ('owner', models.CharField(verbose_name='Vlastník', max_length=40, blank=True)),
                ('type_of_r', models.CharField(verbose_name='Typ památky', max_length=8, blank=True, choices=[('Křížek', 'Křížek'), ('Socha', 'Socha'), ('Jiné', 'Jiné')], null=True)),
                ('sign', models.TextField(verbose_name='Nápis', blank=True, null=True)),
                ('body', models.TextField(verbose_name='Popis')),
                ('katalog_numb', models.CharField(verbose_name='Rejstříkové č.', max_length=30, blank=True)),
                ('series_num', models.IntegerField(verbose_name='Pořadová číslo', blank=True, null=True)),
                ('w_ssr', models.BooleanField(verbose_name='Stezka sovy Rozárky', default=False)),
                ('w_kc', models.BooleanField(verbose_name='Křížková cesta', default=False)),
                ('w_czp', models.BooleanField(verbose_name='Cesta za pověstí', default=False)),
                ('pic', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Titulní foto', upload_to=relic.models.get_name_file, blank=True, null=True)),
                ('pic2', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_2', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic3', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_3', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic4', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_4', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic5', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_5', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic6', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_6', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic7', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_7', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('pic8', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=relic.models.get_name_file, blank=True)),
                ('picd_8', models.CharField(verbose_name='Popis', max_length=100, blank=True, null=True)),
                ('posted', models.DateField(db_index=True, auto_now_add=True)),
                ('slug', models.SlugField(verbose_name='Nechat', max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
