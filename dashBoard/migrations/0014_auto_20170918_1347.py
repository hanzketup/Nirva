# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0013_auto_20170918_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashuser',
            name='offers',
            field=models.ManyToManyField(blank=True, to='dashBoard.Offer'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='expiry',
            field=models.DateTimeField(blank=True),
        ),
    ]