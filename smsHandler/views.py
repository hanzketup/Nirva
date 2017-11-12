# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from .smsClass import Newsms, Newmock
from .sorter import *


def smsIn(request):  # Handles incoming texts from /handler

    sender = request.GET.get('msisdn', None)
    text = request.GET.get('text', None)

    if sender is not None and text is not None:
        sms = Newsms(sender, text)
        primary_sorter(sms)
        return HttpResponse(status=200)
    return HttpResponse(status=200)


def mockIn(request):  # Handles mock messages from /mock

    sender = request.GET.get('num', None)
    text = request.GET.get('text', None)

    if sender is not None and text is not None and text is not '':
        sms = Newmock(sender, text)
        return primary_sorter(sms)

    return HttpResponse("error")