# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=100)),
                ('address', models.CharField(blank=True, max_length=60)),
                ('village', models.CharField(max_length=60)),
                ('district', models.CharField(blank=True, max_length=60)),
                ('region', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=60)),
                ('last', models.CharField(max_length=60)),
                ('nr', models.CharField(max_length=30)),
                ('gps_lat', models.CharField(blank=True, max_length=10)),
                ('gps_long', models.CharField(blank=True, max_length=10)),
                ('lang', models.CharField(default='eng', max_length=5)),
                ('village', models.CharField(blank=True, max_length=60)),
                ('district', models.CharField(blank=True, max_length=60)),
                ('region', models.CharField(blank=True, max_length=60)),
                ('groups', models.ManyToManyField(blank=True, to='userGroup.Group')),
                ('interests', models.ManyToManyField(blank=True, to='userGroup.Interest')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='contact',
            field=models.ManyToManyField(blank=True, to='userGroup.Profile'),
        ),
    ]
