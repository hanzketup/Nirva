from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.apps import apps

DashUser = apps.get_model('dashBoard', 'DashUser')
Profile = apps.get_model('userGroup', 'Profile')


from ..forms import OfferForm

def lister(request):
    if request.user.is_authenticated():
        offers = DashUser.objects.get(user__pk=request.user.pk).offers.all()
        dic = {
            "title":"Offers",
            "offers":offers,

        }

        return render(request,'dashBoard/offer/offers.html', dic)
    else:
        return redirect('/')


def new(request):
    pass


def get(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = DashUser.objects.get(user__pk=request.user.pk).offers.get(pk=pk)

            p = Profile.objects.all()

            dic = {
                'title': 'Offer',
                'profile': q,
                'users': p,

            }
            return render(request, 'dashBoard/offer/showoffer.html', dic)
        else:
            return redirect('/login')

    if request.method == "POST":

        form = ProfileForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            print(cd)

            prof = Profile.objects.get(pk=cd['pk'])

            prof.first = cd['first']
            prof.last = cd['last']
            prof.nr = cd['nr']
            prof.gps_lat = cd['gps_lat']
            prof.gps_long = cd['gps_long']
            prof.lang = cd['lang']
            prof.village = cd['village']
            prof.district = cd['district']
            prof.region = cd['region']

            prof.save()
            return redirect('/profiles/' + cd['pk'])

        else:
            print('bad')
            return redirect('/')