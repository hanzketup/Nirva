import json
import datetime

from django.shortcuts import HttpResponse
from django.apps import apps

DashUser = apps.get_model('dashBoard', 'DashUser')
Offer = apps.get_model('dashBoard', 'Offer')

from .gen_csv import gen_report

def data(request, pk):

    o = Offer.objects.get(pk=pk)

    od = o.alerted.all().count()
    oa = o.answers.all().count()

    # calc percentage
    try:
        odp = 100 / od
    except:
        odp = 0

    pers = int(odp) * int(oa)

    unitt = 0
    for i in o.answers.all():
        unitt = unitt + int(i.value)

    return HttpResponse(json.dumps({
                        "deliv": int(od),
                        "resp": int(oa),
                        "pers": pers,
                        "unit_total": unitt,
                        }))


def get(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Report_{}_{}.csv"'.format(pk, datetime.datetime.now().date())

    gen_report(response, pk)

    return response
