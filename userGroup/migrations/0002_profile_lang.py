# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userGroup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lang',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
