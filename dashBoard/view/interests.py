from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps

Interest = apps.get_model('userGroup', 'Interest')

from ..forms import InterestForm


def lister(request):
    if request.user.is_authenticated():
        interests = Interest.objects.all()

        for i in list(interests):  # Clean out non-completed offers before rendering
            if i.name == '':
                i.delete()

        interest = Interest.objects.all()
        dic = {
            "title": "Interest",
            "interests": interest,
        }

        return render(request, 'dashBoard/interest/interests.html', dic)
    else:
        return redirect('/')


def new(request, pk=None):
    if request.method == "GET":
        if request.user.is_authenticated():

            q = Interest()
            q.save()

            return redirect('/interests/' + str(q.pk) + '/')  # here
        else:
            return redirect('/login')
    if request.method == "POST":
        return get(request, pk)


def get(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated():
            q = Interest.objects.get(pk=pk)

            dic = {
                'title': 'Interest',
                'interest': q,
            }
            return render(request, 'dashBoard/interest/showinterests.html', dic)
        else:
            return redirect('/login')

    if request.method == "POST":

        form = InterestForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            inte = Interest.objects.get(pk=cd['pk'])
            inte.name = cd['name']
            inte.save()

            return redirect('/interests/' + cd['pk'])

        else:
            return HttpResponse("Something went wrong when processing the form")


def remove(request, pk):
    if request.user.is_authenticated():
        q = Interest.objects.get(pk=pk)
        q.delete()
        
        return redirect('/interests')

    else:
        redirect('/')