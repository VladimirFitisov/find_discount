from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Cтартовая страница</h1>')