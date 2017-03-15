from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    context = {'categories': categories}
    return render(request, 'rango/index.html', context)


def about(request):
    return HttpResponse("Aici lumea vorbeste despre ea<br><a href='/rango/'>Acasa</a>")
