# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .smsClass import newSms
from .smsFunc import *

def smsIn(request):  #Handles incomming texts from /handler

    sender = request.GET.get('msisdn', '')
    text = request.GET.get('text', '')

    if sender != '' and text != '':
        sms = newSms(sender, text)
        smsSorter(sms)
        return HttpResponse(status=200)
    return HttpResponse(status=400)