# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

from .gencode import get_code

class DashUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    offers = models.ManyToManyField('Offer', blank=True)

    def __str__(self):
        return str(self.user)


class Offer(models.Model):
    name = models.CharField(max_length=60, default='')
    active = models.BooleanField(default=False)

    message = models.CharField(max_length=300)
    code = models.CharField(max_length=10, default='0')
    unit = models.CharField(max_length=50)

    gen_message = models.CharField(max_length=300, blank=True)

    answers = models.ManyToManyField('Answer', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    expiry_in = models.CharField(max_length=10, blank=True, default=10)
    expiry = models.DateTimeField(blank=True, null=True)

    selected = models.ManyToManyField('userGroup.Profile',
                                      blank=True, related_name='selected')  # users selected in ui, but not alerted
    alerted = models.ManyToManyField('userGroup.Profile',
                                     blank=True, related_name='alerted')  # users that has been alerted, independently from selected_users

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Offer, self).save(*args, **kwargs)

        if self.code == '0':
            self.code = get_code()

        self.expiry = self.created + timedelta(days=float(self.expiry_in))
        super(Offer, self).save(*args, **kwargs)


class Answer(models.Model):
    user = models.ManyToManyField('userGroup.Profile')
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.first().first) + str(self.user.first().last)
