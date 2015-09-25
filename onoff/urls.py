from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'onoff.views.index', name='index'),
                       url(r'login/', 'onoff.views.login_user', name='login'),
                       url(r'^luz/$', 'onoff.views.luz', name='luz'),
                       url(r'^puerta/$', 'onoff.views.puerta', name='puerta'),
                       url(r'^habitacion/$', 'onoff.views.habitacion', name='habitacion'),
                       url(r'^sanitario/(?P<id_sanitario>[0-9]+)/$', 'onoff.views.sanitario', name='sanitario'),
                       url(r'logout/', 'onoff.views.logout_user', name='logout'),
                       url(r'^alarma/(?P<id_alarma>[0-9]+)/$', 'onoff.views.alarma', name='alarma'),
                      )
