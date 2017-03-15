from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    most_viewed_pages = Page.objects.order_by('-views')[:5]
    context = {'categories': categories,
               'most_viewed_pages': most_viewed_pages}
    return render(request, 'rango/index.html', context)


def show_category(request, slug):
    try:
        cat = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        cat = None
    context = {'category': cat}
    return render(request, 'rango/category.html', context)


def about(request):
    return HttpResponse("Aici about<br><a href='/rango/'>Acasa</a>")
