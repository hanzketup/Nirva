# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userGroup', '0008_auto_20170915_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]