# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class DashUser(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    offers = models.ManyToManyField('Offer', blank=True)

    def __str__(self):
        return str(self.user)


class Offer(models.Model):

    name = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    answers = models.ManyToManyField('Answer', blank=True)

    def __str__(self):
        return self.name


class Answer(models.Model):

    user = models.OneToOneField('userGroup.Profile')
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
