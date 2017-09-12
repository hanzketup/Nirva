# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)

    nr = models.CharField(max_length=30)

    gps_lat = models.CharField(blank=True,max_length=10)
    gps_long = models.CharField(blank=True,max_length=10)

    village = models.CharField(blank=True,max_length=60)
    district = models.CharField(blank=True,max_length=60)
    region = models.CharField(blank=True,max_length=60)

    def __str__(self):
      return 'User: ' + self.first + ' : ' + self.nr



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class Group(models.Model):
    pass
