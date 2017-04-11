from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm


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


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, cat_slug):
    try:
        category = Category.objects.get(slug=cat_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, cat_slug)
            else:
                return show_category(request, category)
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)


def about(request):
    return HttpResponse("Aici about<br><a href='/rango/'>Acasa</a>")


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, user_profile_form.errors)
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    return render(request,
                  'rango/register.html',
                  {'user_form': user_form,
                   'user_profile_form': user_profile_form,
                   'registered': registered})
