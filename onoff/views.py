# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from onoff.models import Luz, Puerta, Habitacion, Sanitario, Alarma, Usuario
import time
from django.contrib.auth import authenticate
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import relay_functions
# Create your views here.

def onoff(request):
    context = RequestContext(request)
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    for luz in luces:
        luz_aux= Luz.objects.get(id = luz.id)
        luz_aux.status = relay_functions.getStatus(luz.pin)
        luz_aux.save()
    for puerta in puertas:
        puerta_aux= Puerta.objects.get(id = puerta.id)
        puerta_aux.status = relay_functions.getStatus(puerta.pin)
        puerta_aux.save()
    for alarma in luces:
        alarma_aux= Luz.objects.get(id = alarma.id)
        alarma_aux.status = relay_functions.getStatus(alarma.pin)
        alarma_aux.save()

    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()

    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

def luz(request, id_luz):
    context = RequestContext(request)
## Codigo para que prenda y apage la luz
##  
    print "ahi viene" 
    lista_permitidos = Usuario.objects.filter(permisos_luces=id_luz)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                luz = Luz.objects.get(id = id_luz)
                if luz.status:
                    #relay_functions.luz("close",luz.pin)
                    luz.status = False
                else:
                    #relay_functions.luz("open",luz.pin)
                    luz.status = True
                luz.save()
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

def puerta(request, id_puerta):
    context = RequestContext(request)
    puerta = Puerta.objects.get(id = id_puerta)
    lista_permitidos = Usuario.objects.filter(permisos_puertas=id_puerta)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                print "TRUEEE"
                if puerta.status:
                    relay_functions.puerta("close",puerta.pin)
                    puerta.status = False
                else:
                    relay_functions.puerta("open",puerta.pin)
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
    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

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
    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)


def habitacion(request, id_habitacion):
    context = RequestContext(request)
    ##
    habitacion = Habitacion.objects.get(id = id_habitacion)
    lista_permitidos = Usuario.objects.filter(permisos_habitaciones=id_habitacion)
    if lista_permitidos.__str__() != "[]":
        for permitido in lista_permitidos:
            if permitido.user.id == request.user.id:
                print "TRUEEE"
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
    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)


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
    return render_to_response('onoff.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)
