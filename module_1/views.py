from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions


def index(request):
    if request.user.is_authenticated():
        context = RequestContext(request)
        return render_to_response('index.html',
                              context)

    else:
        context = RequestContext(request)
        return render_to_response('login.html',
                              context)

@requires_csrf_token
def login_user(request):
    
    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = RequestContext(request)
                return render_to_response('index.html',
                              context)
            else:
                context = RequestContext(request)
                return render_to_response('login.html',
                              context)
        else:
            context = RequestContext(request)
            return render_to_response('login.html',
                              context)
    else:
        context = RequestContext(request)
        return render_to_response('login.html',
                              context)

a=False
=======
a=True
>>>>>>> d0dff5b4999592ce2a0fc37e3b0b58dc759f78f1
def abrirPuerta(request):
    if a:
        relay_functions.puerta("open")
        a=False
    else:
        relay_functions.puerta("close")
        a=True

    return render_to_response('index.html',
                             context)
