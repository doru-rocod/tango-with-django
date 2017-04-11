from django.conf.urls import url

from rango import views

app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<cat_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^category/(?P<slug>[\w\-]+)/$',
        views.show_category, name="category"),
    url(r'^register/$', views.register, name='register'),
    url(r'login/$', views.user_login, name='login'),
    url(r'logout/$', views.user_logout, name='logout'),
]
