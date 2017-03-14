import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango.settings')

import django

django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}]
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}]
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}]
    cats = {"Python": {"likes": 64, "views": 128, "pages": python_pages},
            "Django": {"likes": 32, "views": 64, "pages": django_pages},
            "Other Frameworks": {"likes": 16, "views": 32, "pages": other_pages}}
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['likes'], cat_data['views'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print out the categories we added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("{0} -- {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    page = Page.objects.get_or_create(category=cat, title=title)[0]
    page.url = url
    page.views = views
    page.save()
    return page


def add_cat(name, likes, views):
    cat = Category.objects.get_or_create(name=name)[0]
    cat.likes = likes
    cat.views = views
    cat.save()
    return cat


# Start execution here!
if __name__ == '__main__':
    print("Starting rango-population script...")
    populate()
