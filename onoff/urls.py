from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'onoff.views.index', name='indexon'),
                       url(r'login/', 'onoff.views.login_user', name='loginon'),
                       url(r'^luz/$', 'onoff.views.luz', name='luzon'),
                       url(r'^puerta/$', 'onoff.views.puerta', name='puertaon'),
                       url(r'^habitacion/$', 'onoff.views.habitacion', name='habitacionon'),
                       url(r'^sanitario/(?P<id_sanitario>[0-9]+)/$', 'onoff.views.sanitario', name='sanitarioon'),
                       url(r'logout/', 'onoff.views.logout_user', name='logouton'),
                       url(r'^alarma/(?P<id_alarma>[0-9]+)/$', 'onoff.views.alarma', name='alarmaon'),
                       url(r'addroom/', 'onoff.views.add_room', name='addroomon'),
                      )
