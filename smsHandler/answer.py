import re

from django.apps import apps

from .lang import langresolver as lr

Offer = apps.get_model('dashBoard', 'Offer')
Answer = apps.get_model('dashBoard', 'Answer')


def create_answer(sms):

    try:
        quantity = (re.search(r'.+ (\d+)', sms.message)).group(0)

    except:
        return sms.respond(lr.msg('inr', sms.lang))

    an = Answer(user=sms.user, value=quantity)
    of = Offer.objects.get(code=sms.kw).answers.add(an)

    return sms.respond()