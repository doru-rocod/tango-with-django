from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Cea mai buna portocala!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Aici lumea vorbeste despre ea<br><a href='/rango/'>Acasa</a>")
