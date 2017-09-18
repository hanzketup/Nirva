from django.core.exceptions import ObjectDoesNotExist

import re
import requests

from django.apps import apps
from .models import smsLogger

from .dispatcher import dispatch

Profile = apps.get_model('userGroup', 'Profile')

"""


"""

class newSms():

    def __init__(self, sender, message):

        self.sender = sender
        self.message = message
        self.kw = (re.search(r'^(\S+)',message)).group(0)

        try:
            self.user = Profile.objects.get(nr=self.sender)
            self.is_user = True

        except ObjectDoesNotExist:
            self.is_user = False

        #standard values
        self.firstName = ""
        self.lastName = ""
        self.fullName = ""
        self.lang = "eng"

        if self.is_user: #if the user is in the system
            self.firstName = self.user.first
            self.lastName = self.user.last
            self.fullName = self.user.first + " " + self.user.last
            self.lang = self.user.lang


    def respond(self, msg):
        r = dispatch(self.nr, msg)
        self.Log(msg, r)


    def Log(self, message, response):
        log = smsLogger(number=self.sender,
                        msg=self.message,
                        resp_msg=message,
                        name=self.fullName,
                        api_resp=response,
                        )
        log.save()