# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0028_auto_20170921_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashuser',
            name='offers',
            field=models.ManyToManyField(blank=True, to='dashBoard.Offer'),
        ),
    ]
