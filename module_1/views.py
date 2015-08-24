from django.shortcuts import render_to_response, render
from django.template import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
