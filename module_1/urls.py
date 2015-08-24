from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'module_1.views.index', name='index'),
                       )
