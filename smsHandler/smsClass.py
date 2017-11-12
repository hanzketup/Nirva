from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse

import re
import requests

from django.apps import apps
from .dispatcher import dispatch

Profile = apps.get_model('userGroup', 'Profile')
Log = apps.get_model('smsHandler', 'Log')

"""


"""


class Newsms():
    def __init__(self, sender, message):

        self.sender = sender
        self.message = message.lower()
        self.kw = (re.search(r'^(\S+)', message)).group(0)

        try:
            self.user = Profile.objects.get(nr=self.sender)
            self.is_user = True

        except ObjectDoesNotExist:
            self.is_user = False

    def respond(self, msg):
        r = dispatch(self.sender, msg)
        print('response sent to {}'.format(self.sender))
        self.log(msg, r)

    def log(self, message, response):

        name = ''

        if self.is_user:
            name = self.user.first + self.user.last

        log = Log(number=self.sender,
                  msg=self.message,
                  resp_msg=message,
                  name=name,
                  api_resp=response,
                  )
        log.save()


class Newmock():
    def __init__(self, sender, message):

        self.sender = sender
        self.message = message.lower()
        self.kw = (re.search(r'^(\S+)', message)).group(0)

        try:
            self.user = Profile.objects.get(nr=self.sender)
            self.is_user = True

        except ObjectDoesNotExist:
            self.is_user = False

    def respond(self, msg):
        return HttpResponse(msg)

    def log(self, message, response):
        pass