# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsHandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smslogger',
            name='api_resp',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='smslogger',
            name='resp_msg',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]