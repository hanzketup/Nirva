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

            groups_checked = []
            inters_checked = []

            for e in q:
                for i in e.groups.all():
                    groups_checked.append(int(i.pk))

                for i in e.interests.all():
                    inters_checked.append(int(i.pk))

            dic = {
                'title': 'User Profile',
                'profile': q,

                'group': group,
                'inter': inter,

                'selgroup': str(groups_checked),
                'selinters': str(inters_checked),

            }

            print(inters_checked)

            return render(request, 'dashBoard/profile/showprofile.html', dic)
        else:
            return redirect('/login')

    if request.method == "POST":

        form = ProfileForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            print(cd['group'][1:-1].split(','))

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

            prof.interests.clear()  # Clear manytomany field and add new ones passed in.
            for i in cd['inter'].replace('[', '').replace(']', '').split(','):
                if i != '' and i != 'null':
                    prof.interests.add(i)

            prof.groups.clear()  # Clear manytomany field and add new ones passed in.
            for i in cd['group'].replace('[', '').replace(']', '').split(','):
                if i != '' and i != 'null':
                    prof.groups.add(i)

            prof.save()
            return redirect('/profiles/' + cd['pk'])

        else:
            return redirect('/')


def remove(request, pk):
    if request.user.is_authenticated():
        q = Profile.objects.get(pk=pk)
        q.delete()

        return redirect('/profiles')

    else:
        redirect('/')
