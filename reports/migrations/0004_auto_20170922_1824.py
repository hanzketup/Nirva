# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170915_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='data',
            field=models.CharField(max_length=1000),
        ),
    ]
