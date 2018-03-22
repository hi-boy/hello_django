# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def hello_django(request):
    """
    hello_django
    :param request:
    :return:
    """
    return HttpResponse('hello_django')


def url_name(request, a, b):
    """
    url 路径传参      http://127.0.0.1:8000/url_name/6/7
    :param request:
    :param a:
    :param b:
    :return:
    """
    c = int(a) + int(b)
    return HttpResponse(c)

def url_get(request):
    """
    get 传参         http://127.0.0.1:8000/url_get?a=5&b=6
    :param request:
    :return:
    """
    a = request.GET['a']
    b = request.GET.get('b')
    c = int(a) + int(b)

    return HttpResponse(str(c))


def post_html(request):
    return render(request, 'url/post.html', locals())

def url_post(request):
    """
    post 传参
    :param request:
    :return:
    """
    result = {}
    a = request.POST['a']
    b = request.POST.get('b')
    likes = request.POST.getlist('like')   #获取一个数组
    result['a'] = a
    result['b'] = b
    result['likes'] = likes
    return HttpResponse(json.dumps(result), content_type="application/json")

