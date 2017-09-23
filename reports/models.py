# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class report(models.Model):

    name = models.CharField(max_length=100,default="Standard report")
    data = models.CharField(max_length=1000)

    answers = models.CharField(max_length=60,default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " : " + str(self.created)