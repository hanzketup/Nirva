# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import sys

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.apps import apps

from smsHandler import dispatcher

Profile = apps.get_model('userGroup', 'Profile')
Group = apps.get_model('userGroup', 'Group')
interest = apps.get_model('userGroup', 'interest')

DashUser = apps.get_model('dashBoard', 'DashUser')
Offer = apps.get_model('dashBoard', 'Offer')

Log = apps.get_model('smsHandler', 'Log')
Eventlog = apps.get_model('smsHandler', 'Eventlog')


def Home(request):
    if request.user.is_authenticated():

        offers = Offer.objects.all()

        for i in list(offers):  # Clean out non-completed offers before rendering
            if i.name == '':
                i.delete()
            print(i)

        offers = Offer.objects.all()

        dic = {
            'title': 'Home',
            'user': request.user,
            'offers': offers[::-1],

        }
        return render(request, 'dashBoard/home.html', dic)
    else:
        return redirect('/login')


def loginV(request):
    if request.method == "GET":

        if request.user.is_authenticated():
            return redirect('/')
        else:
            dic = {
                "title": "Login",
            }
            return render(request, 'dashBoard/login.html', dic)

    elif request.method == "POST":
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            dic = {
                'title': 'login',
                'inborder': 'border-bottom: 4px solid #c0392b;',
                'login_msg': 'Username/Password incorrect',

            }
            return render(request, 'dashBoard/login.html', dic)


def logoutV(request):
    logout(request)
    return redirect('/login')


def settings(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            dic = {
                'title': 'Settings',
                'ver': sys.version_info,
            }
            return render(request, 'dashBoard/settings.html', dic)

        if request.method == 'POST':
            u = User.objects.get(pk=request.user.pk)
            u.set_password(request.POST.get('pwd'))
            u.save()

            return redirect('/')


def dispatch(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            q = Profile.objects.all()

            dic = {
                'title': 'Send Message',
                'users': q,
            }
            return render(request, 'dashBoard/dispatcher/dispatch.html', dic)

        if request.method == 'POST':
            try:
                reqdata = json.loads(request.body.decode("UTF-8"))
                msg = reqdata['msg']
                numlist = []

                print(reqdata['pk'])

                for i in reqdata['pk']:
                    r = Profile.objects.get(pk=str(i)).nr
                    numlist.append(str(r))

            except:
                return HttpResponse("Something went wrong, message failed")

            dispatcher.mass(numlist, msg)
            return HttpResponse("Message sent!")


def log(request):
    if request.user.is_authenticated():
        logs = Log.objects.all()

        dic = {
            'title': 'Logger',
            'logs': logs[::-1],
        }
        return render(request, 'dashBoard/dispatcher/log.html', dic)


def mock(request):
    if request.user.is_authenticated():
        dic = {
            'title': 'Mock',
        }
        return render(request, 'dashBoard/mock.html', dic)


def events(request):
    if request.user.is_authenticated():
        logs = Eventlog.objects.all()

        dic = {
            'title': 'Event Logger',
            'logs': logs[::-1],
        }
        return render(request, 'dashBoard/eventlog.html', dic)


def help(request):
    if request.user.is_authenticated():
        dic = {
            'title': 'Help',
        }
        return render(request, 'dashBoard/help.html', dic)
