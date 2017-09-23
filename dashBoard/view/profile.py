from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.apps import apps

Group = apps.get_model('userGroup', 'Group')
interest = apps.get_model('userGroup', 'interest')

Profile = apps.get_model('userGroup', 'Profile')

from ..forms import ProfileForm


def lister(request):
    if request.user.is_authenticated():
        profiles = Profile.objects.all()

        for i in list(profiles):  # Clean out non-completed offers before rendering
            if i.first == '':
                i.delete()

        q = Profile.objects.all()
        dic = {
            'title': 'Profiles',
            'profiles': q,

        }
        return render(request, 'dashBoard/profile/profiles.html', dic)
    else:
        return redirect('/login')


def new(request, pk=None):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Profile()
            q.save()

            return redirect('/profiles/' + str(q.pk) + '/')  # here
        else:
            return redirect('/login')

    if request.method == "POST":
        get(request, pk)


def get(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated():

            group = Group.objects.all()
            inter = interest.objects.all()

            q = Profile.objects.filter(pk=pk)
            dic = {
                'title': 'User Profile',
                'profile': q,

                'group':group,
                'inter':inter,

            }
            return render(request, 'dashBoard/profile/showprofile.html', dic)
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


def remove(request, pk):
    if request.user.is_authenticated():
        q = Profile.objects.get(pk=pk)
        q.delete()

        return redirect('/profiles')

    else:
        redirect('/')
