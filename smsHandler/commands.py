import re

from django.apps import apps

from .lang import langresolver as lr

Offer = apps.get_model('dashBoard', 'Offer')
Answer = apps.get_model('dashBoard', 'Answer')


def commandsorter(sms):
    kw = sms.kw
    if kw == '*c':
        return cancel(sms)

    if kw == '*me':
        return sms.respond(sms.user.first + ' ' + sms.user.last)

    if kw == '*info' or kw == '*help':
        return sms.respond(lr.msg('info', sms.user.lang))

    else:
        return sms.respond(lr.msg('cnf', sms.user.lang))


def cancel(sms):  # cancel answer to offer

    try:
        code = (re.search(r'^\S+ (.+)', sms.message)).group(1)
    except:
        return sms.respond(lr.msg('nv', sms.user.lang))

    ofr = Offer.objects.get(code=code)

    if ofr.active:

        ans = ofr.answers.get(user=sms.user)
        ofr.answers.remove(ans)
        ans.delete()

        return sms.respond(lr.msg('arm', sms.user.lang))

    else:
        return sms.respond(lr.msg('nact', sms.user.lang))
