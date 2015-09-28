from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'module_1.views.index', name='index'),
                       url(r'login/', 'module_1.views.login_user', name='login'),
                       url(r'^luz/$', 'module_1.views.luz', name='luz'),
                       url(r'^puerta/$', 'module_1.views.puerta', name='puerta'),
                       url(r'^habitacion/$', 'module_1.views.habitacion', name='habitacion'),
                       url(r'^sanitario/(?P<id_sanitario>[0-9]+)/$', 'module_1.views.sanitario', name='sanitario'),
                       url(r'logout/', 'module_1.views.logout_user', name='logout'),
                       url(r'^alarma/(?P<id_alarma>[0-9]+)/$', 'module_1.views.alarma', name='alarma'),
                       url(r'info/$', 'module_1.views.send_hello_world', name='holaMundo'),
                      )
