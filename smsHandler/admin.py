# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

admin.site.register(models.Log)
admin.site.register(models.Eventlog)