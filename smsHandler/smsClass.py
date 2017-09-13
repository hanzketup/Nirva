import re
import requests

from userGroup import models
from .models import smsLogger

"""


"""

class newSms():

    def __init__(self, sender, message):

        self.sender = sender
        self.message = message
        self.kw = (re.search(r'^(\S+)',message)).group(0)

        self.user = models.Profile.objects.filter(nr=self.sender)
        self.is_user = self.user.exists()

        #standard values
        self.firstName = ""
        self.lastName = ""
        self.fullName = ""
        self.lang = "eng"

        if self.is_user: #if the user is in the system
            self.firstName = self.user.first
            self.lastName = self.user.last
            self.fullName = (self.user.first," ", self.user.last)


    def respond(self, msg):
        r = requests.post('https://rest.nexmo.com/sms/json',
                          data={"to": self.sender,
                                "from": "46769436405",
                                "text": msg,
                                "api_key": "76e3575b",
                                "api_secret": "2ca2ac5f9a6520ff", }, timeout=5)
        self.Log(msg, r.text)


    def Log(self, message, response):
        log = smsLogger(number=self.sender,
                        msg=self.message,
                        resp_msg=message,
                        name=self.fullName,
                        api_resp=response,
                        )
        log.save()