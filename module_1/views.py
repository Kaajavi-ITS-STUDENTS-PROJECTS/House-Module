from django.shortcuts import render_to_response, render
from django.template import RequestContext
import relay_functions

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)

def abrirPuerta(request):
    relay_functions.puerta("open")
    return render_to_response('index.html',
                             context)
