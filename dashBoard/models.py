# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class DashUser(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    offers = models.ManyToManyField('Offer', blank=True)

    def __str__(self):
        return str(self.user)


class Offer(models.Model):

    name = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    message = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    unit = models.CharField(max_length=50)


    answers = models.ManyToManyField('Answer', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(blank=True, null=True)

    reports = models.ManyToManyField('reports.Report', blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        super(Offer, self).save(*args, **kwargs)
        self.expiry = self.created + timedelta(days=10)
        super(Offer, self).save(*args, **kwargs)


class Answer(models.Model):

    user = models.ManyToManyField('userGroup.Profile')
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
