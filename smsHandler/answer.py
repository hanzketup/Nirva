import re

from django.apps import apps

from .lang import langresolver as lr
from .lang.langresolver import generate_confirm

Offer = apps.get_model('dashBoard', 'Offer')
Answer = apps.get_model('dashBoard', 'Answer')


def create_answer(sms):
    of = Offer.objects.get(code=sms.kw)

    if of.active:

        try:
            quantity = (re.search(r'.+ (\d+)', sms.message)).group(1)

        except:
            return sms.respond(lr.msg('nv', sms.user.lang))

        prev = Offer.objects.get(code=sms.kw).answers.filter(user__pk=sms.user.pk)

        if not prev.exists():

            an = Answer(value=quantity)
            an.save()
            an.user.add(sms.user)
            an.save()

            Offer.objects.get(code=sms.kw).answers.add(an)

            return sms.respond(generate_confirm(of.code))

        else:
            prevs = prev.first()
            prevs.value = quantity
            prevs.save()
            return sms.respond(lr.msg('au', sms.user.lang))

    else:
        return sms.respond(lr.msg('nact', sms.user.lang))