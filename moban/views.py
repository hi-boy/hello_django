# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def moban(request):
    return render(request, 'moban/1.html', locals())