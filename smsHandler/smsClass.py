import re
from userGroup import models

class newSms():

    def __init__(self, sender, message):

        self.sender = sender
        self.message = message
        self.kw = (re.search(r'^(\S+)',message)).group(0)

        self.user = models.Profile.objects.filter(nr=self.sender)

        self.is_user = self.user.exists()

        self.firstName = self.user.first
        self.lastName = self.user.last

