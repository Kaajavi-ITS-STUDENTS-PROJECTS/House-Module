from django.shortcuts import render_to_response, render
from django.template import RequestContext
import relay_functions

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
a=True
def abrirPuerta(request):
    if a:
        relay_functions.puerta("open")
        a=False
    else:
        relay_functions.puerta("close")
        a=True

    return render_to_response('index.html',
                             context)
