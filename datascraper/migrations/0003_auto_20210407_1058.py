# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-04-07 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0002_auto_20210407_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
