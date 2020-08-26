# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sleepy
# from time import sleep
from django.core.cache import cache
import redis_cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
def send_email(request):
    sleepy.delay(10)
    return HttpResponse("Success")

def cache_test(request):
    cache.set('my_key', 'helloworld', timeout=CACHE_TTL)
    print(cache.get('my_key'))
    return HttpResponse("done")
