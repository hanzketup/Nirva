from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps

import json

DashUser = apps.get_model('dashBoard', 'DashUser')
Offer = apps.get_model('dashBoard', 'Offer')

Profile = apps.get_model('userGroup', 'Profile')

from smsHandler.lang.langresolver import generate_tail
from smsHandler.tasks import dispatch_offers

from ..forms import OfferForm


def lister(request):
    if request.user.is_authenticated():
        offers = Offer.objects.all()

        for i in list(offers):  # Clean out non-completed offers before rendering
            if i.name == '':
                i.delete()

        offers = Offer.objects.all()
        dic = {
            "title":"Offers",
            "offers":offers[::-1],

        }

        return render(request,'dashBoard/offer/offers.html', dic)
    else:
        return redirect('/')


def new(request, pk=None):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Offer()
            q.save()

            return redirect('/offers/' + str(q.pk) + '/')  # here
        else:
            return redirect('/login')
    if request.method == "POST":
        return get(request, pk)


def get(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Offer.objects.get(pk=pk)

            p = Profile.objects.all()

            dic = {
                'title': 'Offer',
                'offer': q,
                'users': p,

            }
            return render(request, 'dashBoard/offer/showoffer.html', dic)
        else:
            return redirect('/login')

    if request.method == "POST":

        form = OfferForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            act = bol(cd['active'])

            off = Offer.objects.get(pk=cd['pk'])

            off.name = cd['name']
            off.active = act

            off.expiry_in = cd['expiry']
            off.message = cd['message']
            off.unit = cd['unit']

            off.gen_message = cd['message'] + generate_tail(off.code, cd['unit'], off.expiry)

            off.save()

            dispatch_offers.delay()

            return redirect('/offers/' + cd['pk'])

        else:
            return HttpResponse("Something went wrong when processing the form")


def save(request, pk):
    if request.method == "GET":
       return redirect('/')

    if request.method == "POST":

        try:
            pklist = json.loads(request.body.decode("utf-8"))['pk'] # bytestring > unicode > json

        except:
            return HttpResponse("Wrong data")

        r = Offer.objects.get(pk=pk)
        r.selected.remove()
        r.selected.clear()
        r.selected.add(*pklist)

        return HttpResponse("Users changed!")

def remove(request, pk):
    if request.user.is_authenticated():
        q = Offer.objects.get(pk=pk)
        q.delete()

        return redirect('/offers')

    else:
        redirect('/')


# non-standard functions

def bol(s):
    if s == '1':
        return True
    else:
        return False