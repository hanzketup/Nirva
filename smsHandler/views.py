# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .smsClass import newSms
from .smsFunc import *

def smsIn(request):  #Handles incomming texts from /handler

    sender = request.GET.get('msisdn', None)
    text = request.GET.get('text', None)

    if sender is not None and text is not None:
        sms = newSms(sender, text)
        smsSorter(sms)
        return HttpResponse(status=200)
    return HttpResponse(status=400)