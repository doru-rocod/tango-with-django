from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Salutare, bostane!<br><a href='/rango/about'>Despre</a>")


def about(request):
    return HttpResponse("Aici bostanul vorbeste despre el<br><a href='/rango/'>Acasa</a>")
