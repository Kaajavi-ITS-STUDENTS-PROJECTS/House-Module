from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions
import relay_status
from module_1.models import Luz, Puerta, Habitacion, Sanitario, Alarma
import time
# Create your views here.

def index(request):
    if request.user.is_authenticated():
        context = RequestContext(request)
        luces = Luz.objects.all()
        puertas = Puerta.objects.all()
        habitaciones = Habitacion.objects.all()
        habitaciones = Habitacion.objects.all()
        sanitarios = Sanitario.objects.all()
        alarmas = Alarma.objects.all()
        for luz in luces:
            luz_aux= Luz.objects.get(id = luz.id)
            luz_aux.status = relay_status.getStatus(luz.pin)
            luz_aux.save()
        for puerta in puertas:
            puerta_aux= Puerta.objects.get(id = puerta.id)
            puerta_aux.status = relay_status.getStatus(puerta.pin)
            puerta_aux.save()
        for alarma in luces:
            alarma_aux= Luz.objects.get(id = alarma.id)
            alarma_aux.status = relay_status.getStatus(alarma.pin)
            alarma_aux.save()

        luces = Luz.objects.all()
        puertas = Puerta.objects.all()
        habitaciones = Habitacion.objects.all()
        habitaciones = Habitacion.objects.all()
        sanitarios = Sanitario.objects.all()
        alarmas = Alarma.objects.all()

        return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)
    else:
        context = RequestContext(request)
        return render_to_response('login.html',
                              context)

def luz(request, id_luz):
    context = RequestContext(request)
## Codigo para que prenda y apage la luz
##
    luz = Luz.objects.get(id = id_luz)
    if luz.status:
        relay_functions.relay("close",luz.pin)
        luz.status = False
    else:
        relay_functions.relay("open",luz.pin)
        luz.status = True
    luz.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

def puerta(request, id_puerta):
    context = RequestContext(request)
    puerta = Puerta.objects.get(id = id_puerta)
    if puerta.status:
        relay_functions.relay("close",puerta.pin)
        puerta.status = False
    else:
        relay_functions.relay("open",puerta.pin)
        puerta.status = True
    puerta.save()
    time.sleep(10)
    puerta = Puerta.objects.get(id = id_puerta)
    if puerta.status:
        ## Codigo para que cierra la puerta
        ##
        puerta.status = False
    else:
        ## Codigo para que abra la puerta
        ##
        puerta.status = True
    puerta.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

def sanitario(request, id_sanitario):
    context = RequestContext(request)
    sanitario = Sanitario.objects.get(id = id_sanitario)
    if sanitario.ocupado:
        sanitario.ocupado = False
    else:
        sanitario.ocupado = True
    sanitario.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)


def habitacion(request, id_habitacion):
    context = RequestContext(request)
    ##
    habitacion = Habitacion.objects.get(id = id_habitacion)
    if habitacion.status:
        habitacion.status = False
    else:
        habitacion.status = True
    luces = Luz.objects.filter(lugar_id = id_habitacion)


    for luz in luces:
        ##Codigo para que apage cada una de las luces del for
        luz.status = habitacion.status
        luz.save()

    habitacion.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)


def alarma(request, id_alarma):
    context = RequestContext(request)
    ## Codigo para que suene la chichasha
    ##
    alarma = Alarma.objects.get(id = id_alarma)
    ##Todo para que suene y etc
    alarma.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

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

