from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.index, name='index'),
    url(r'^map.html/$', views.index, name='index')
]
