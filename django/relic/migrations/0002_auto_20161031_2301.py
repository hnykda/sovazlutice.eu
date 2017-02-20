# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relic',
            name='w_csj',
            field=models.BooleanField(default=False, verbose_name='Cesta sv. Jakuba'),
        ),
        migrations.AddField(
            model_name='relic',
            name='w_div',
            field=models.BooleanField(default=False, verbose_name='Cesta divočinou'),
        ),
    ]
