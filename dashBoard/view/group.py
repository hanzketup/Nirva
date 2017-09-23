from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps

Group = apps.get_model('userGroup', 'Group')
Profile = apps.get_model('userGroup', 'Profile')

from ..forms import GroupForm


def lister(request):
    if request.user.is_authenticated():
        groups = Group.objects.all()

        for i in list(groups):  # Clean out non-completed offers before rendering
            if i.village == '':
                i.delete()

        groups = Group.objects.all()
        dic = {
            "title": "Groups",
            "groups": groups,

        }

        return render(request, 'dashBoard/group/groups.html', dic)
    else:
        return redirect('/')


def new(request, pk=None):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Group()
            q.save()

            return redirect('/groups/' + str(q.pk) + '/')  # here
        else:
            return redirect('/login')
    if request.method == "POST":
        return get(request, pk)


def get(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Group.objects.get(pk=pk)
            p = Profile.objects.all()

            dic = {
                'title': 'Group',
                'group': q,
                'users': p,
            }
            return render(request, 'dashBoard/group/showgroup.html', dic)
        else:
            return redirect('/login')

    if request.method == "POST":

        form = GroupForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            gro = Group.objects.get(pk=cd['pk'])

            gro.address = cd['address']
            gro.village = cd['village']
            gro.district = cd['district']
            gro.region = cd['region']

            gro.save()

            return redirect('/groups/' + cd['pk'])

        else:
            return HttpResponse("Something went wrong when processing the form")


def remove(request, pk):
    if request.user.is_authenticated():
        q = Group.objects.get(pk=pk)
        q.delete()

        return redirect('/groups')

    else:
        redirect('/')


def save(request, pk):
    if request.method == "GET":
        return redirect('/')

    if request.method == "POST":

        try:
            reqdata = json.loads(request.body)['pk']

        except:
            return HttpResponse("Wrong data")

        data = reqdata[0]
        r = Group.objects.get(pk=pk)
        p = Profile.objects.get(pk=data)

        r.contact.remove()

        r.contact.add(p)

        return HttpResponse("data added")
