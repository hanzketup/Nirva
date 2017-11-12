# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Log(models.Model):

    number = models.CharField(max_length=60)
    msg = models.CharField(max_length=500)
    resp_msg = models.CharField(max_length=500)

    time = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=True, max_length=100)

    api_resp = models.CharField(blank=True,max_length=500)

    def __str__(self):
        return self.name + ' : ' + self.number


class Eventlog(models.Model):

    name = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name