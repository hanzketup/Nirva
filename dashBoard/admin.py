# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.DashUser)

admin.site.register(models.Offer)
admin.site.register(models.Answer)
