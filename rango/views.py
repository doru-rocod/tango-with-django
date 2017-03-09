from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Salutare, lume!<br><a href='/rango/about'>Despre</a>")


def about(request):
    return HttpResponse("Aici lumea vorbeste despre ea<br><a href='/rango/'>Acasa</a>")
