# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def moban(request):

    return render(request, 'moban/1.html', locals())

def moban2(requset):

    list = ['java', 'python', 'php']
    result = {'name': '小强', 'age': 26, 'phone': '666666'}
    return render(requset, 'moban/2.html', locals())

