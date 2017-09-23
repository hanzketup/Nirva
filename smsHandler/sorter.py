from django.apps import apps

from .lang import langresolver as lr
from .commands import commandsorter
from .answer import create_answer

Offer = apps.get_model('dashBoard', 'Offer')


def primary_sorter(sms):  #handle and sort valid requests
    q = Offer.objects.all()
    codes = [x.code for x in q]
    if sms.is_user:
        kw = sms.kw
        if kw[0] == '#':
            return commandsorter(sms)

        if any(kw in s for s in codes):
            return create_answer(sms)

        else:
            return sms.respond(lr.msg('cnf', sms.user.lang))

    else:
        return sms.respond(lr.msg('nu'))