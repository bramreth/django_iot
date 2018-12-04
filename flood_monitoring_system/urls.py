from django.conf.urls import url,include
from itertools import chain
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index.html/$', views.index, name='index')
]
