# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.apps import apps

Profile = apps.get_model('userGroup', 'Profile')
Group = apps.get_model('userGroup', 'Group')

DashUser = apps.get_model('dashBoard', 'DashUser')
Offer = apps.get_model('dashBoard', 'Offer')
DashUser = apps.get_model('dashBoard', 'DashUser')

def Home(request):
    if request.user.is_authenticated():

        offers = DashUser.objects.get(user__pk=request.user.pk).offers.all()
        dic = {
            'title': 'Home',
            'user':request.user,
            'offers':offers,

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
                "title":"Login",
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
                'title':'login',
                'inborder': 'border-bottom: 4px solid #c0392b;',
                'login_msg':'Username/Password incorrect',

            }
            return render(request, 'dashBoard/login.html', dic)

def logoutV(request):
    logout(request)
    return redirect('/login')

def offers(request):
    if request.user.is_authenticated():
        offers = DashUser.objects.get(user__pk=request.user.pk).offers.all()
        dic = {
            "title":"Offers",
            "offers":offers,

        }

        return render(request,'dashBoard/offers.html', dic)
    else:
        return redirect('/')

def interests(request):
    if request.user.is_authenticated():
        interests = DashUser.objects.get(user__pk=request.user.pk).offers.all()
        dic = {
            "title":"interests",
            "interests":interests,

        }

        return render(request,'dashBoard/interests.html', dic)
    else:
        return redirect('/')

def reports(request):
    if request.user.is_authenticated():
        reports = DashUser.objects.get(user__pk=request.user.pk).offers.all()
        dic = {
            "title":"Reports",
            "reports":reports,

        }

        return render(request,'dashBoard/reports.html', dic)
    else:
        return redirect('/')

def groups(request):
    if request.user.is_authenticated():
        groups = Group.objects.all()
        dic = {
            "title":"Groups",
            "groups":groups,

        }

        return render(request,'dashBoard/groups.html', dic)
    else:
        return redirect('/')

def contact(request):
    return