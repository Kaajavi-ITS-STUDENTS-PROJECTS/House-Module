from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'module_1.views.index', name='index'),
<<<<<<< HEAD
                       url(r'^$', 'module_1.views.abrirPuerta', name='index'),
                       url(r'login/', 'module_1.views.login_user', name='login'),
=======
                       url(r'^$', 'module_1.views.abrirPuerta', name='abrir'),
>>>>>>> d0dff5b4999592ce2a0fc37e3b0b58dc759f78f1
                       )
