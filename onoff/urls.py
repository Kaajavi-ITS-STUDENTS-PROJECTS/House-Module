# -*- coding: utf-8 -*-
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^luz/(?P<id_luz>[0-9]+)/$', views.luz, name='luz'),
    url(r'^puerta/(?P<id_puerta>[0-9]+)/$', views.puerta, name='puerta'),
    url(r'^habitacion/(?P<id_habitacion>[0-9]+)/$', views.habitacion, name='habitacion'),
    url(r'^sanitario/(?P<id_sanitario>[0-9]+)/$', views.sanitario, name='sanitario'),
    url(r'^alarma/(?P<id_alarma>[0-9]+)/$', views.alarma, name='alarma'),
]