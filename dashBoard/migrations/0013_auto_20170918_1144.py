# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0012_auto_20170918_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='unit',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dashuser',
            name='offers',
            field=models.ManyToManyField(blank=True, to='dashBoard.Offer'),
        ),
    ]