from django.shortcuts import render_to_response, render
from django.template import RequestContext
import relay_functions

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
a=True
def abrirPuerta(request):
    if request.method == 'POST':
        if a:
            relay_functions.relay("open",15)
            a=False
        else:
            relay_functions.relay("close",15)
            a=True

    return render_to_response('index.html',
                             context)
