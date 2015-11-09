from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'module_1.views.index', name='index'),
                       url(r'login/', 'module_1.views.login_user', name='login'),
                       url(r'^luz/$', 'module_1.views.luz', name='luz'),
                       url(r'^puerta/$', 'module_1.views.puerta', name='puerta'),
                       url(r'^habitacion/$', 'module_1.views.habitacion', name='habitacion'),
                       url(r'^hab_get/$', 'module_1.views.hab_get', name='hab_get'),
                       url(r'^sanitario/(?P<id_sanitario>[0-9]+)/$', 'module_1.views.sanitario', name='sanitario'),
                       url(r'logout/', 'module_1.views.logout_user', name='logout'),
                       url(r'^alarma/(?P<id_alarma>[0-9]+)/$', 'module_1.views.alarma', name='alarma'),
                       url(r'autoluz/', 'module_1.views.auto_luz', name='autoluz'),
                       url(r'getcurrentuser/', 'module_1.views.get_current_user', name='getcurrentuser'),
                       url(r'add_rule/', 'module_1.views.add_rule', name='add_rule'),
                      )
