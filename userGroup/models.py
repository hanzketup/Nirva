# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Profile(models.Model):
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)

    nr = models.CharField(max_length=30)

    gps_lat = models.CharField(blank=True, max_length=10)
    gps_long = models.CharField(blank=True, max_length=10)

    lang = models.CharField(default="eng", max_length=5)

    village = models.CharField(blank=True, max_length=60)
    district = models.CharField(blank=True, max_length=60)
    region = models.CharField(blank=True, max_length=60)

    interest = models.ManyToManyField('Interest', blank=True)

    def __str__(self):
        return 'User: ' + self.first + ' : ' + self.nr


class Group(models.Model):
    name = models.CharField(max_length=100, editable=False)

    contact = models.OneToOneField(Profile)

    address = models.CharField(max_length=60)
    village = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    region = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)
        self.name = str(self.village) + ' - ' + str(self.pk)
        super(Group, self).save(*args, **kwargs)


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
