from __future__ import absolute_import
import datetime
from celery import shared_task
from django.apps import apps
from . import dispatcher

Offer = apps.get_model('dashBoard', 'Offer')
Profile = apps.get_model('userGroup', 'Profile')
Eventlog = apps.get_model('smsHandler', 'Eventlog')


@shared_task
def dispatch_offers():

    o = Offer.objects.all()
    ran = {}

    for i in o:
        if i.active:

            sel = [s.pk for s in i.selected.all()]
            alt = [s.pk for s in i.alerted.all()]

            disp = []
            nums = []

            for e in sel: # if the users is not already alerted, add them to disp
                if e not in alt:
                    disp.append(e)

            if disp:
                for v in disp:
                    po = Profile.objects.get(pk=v)
                    i.alerted.add(po)
                    nums.append(po.nr)

                dispatcher.mass(nums, i.gen_message)
                ran[i.pk] = nums

            print('dispatcher ran')

        else:
            continue

    if ran:
        el = Eventlog(name="dispatcher task ran and dispatched offers to {}".format(ran))
        el.save()
    else:
        el = Eventlog(name="dispatcher task ran but no action was required")
        el.save()


@shared_task
def expiry_switch():

    o = Offer.objects.all()

    for i in o:

        if i.expiry > datetime.datetime.now():
            i.active = False
            i.save()
            el = Eventlog(name="Expiry Switch changed {} to false".format(i.name))
            el.save()

        else:
            continue
