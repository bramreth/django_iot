from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index.html/$', views.index, name='index'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^test/$', views.test, name='test'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^subscription/$', views.subscription_process, name='subscription_process'),
    url(r'^readnotification/$', views.readnotification, name='readnotification')
]

