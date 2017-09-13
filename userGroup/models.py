# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)

    nr = models.CharField(max_length=30)

    gps_lat = models.CharField(blank=True,max_length=10)
    gps_long = models.CharField(blank=True,max_length=10)

    lang = models.CharField(default="eng",max_length=5)

    village = models.CharField(blank=True,max_length=60)
    district = models.CharField(blank=True,max_length=60)
    region = models.CharField(blank=True,max_length=60)

    def __str__(self):
      return 'User: ' + self.first + ' : ' + self.nr




class Group(models.Model):
    pass
