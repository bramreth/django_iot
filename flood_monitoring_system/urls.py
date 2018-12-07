from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index.html/$', views.index, name='index'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^test/$', views.test, name='test')
]
