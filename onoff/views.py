# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from onoff.models import Luz, Puerta, Habitacion, Sanitario, Alarma
# Create your views here.

def index(request):
    context = RequestContext(request)
    luces = Luz.objects.all()
    puertas = Puerta.objects.all()
    habitaciones = Habitacion.objects.all()
    habitaciones = Habitacion.objects.all()
    sanitarios = Sanitario.objects.all()
    alarmas = Alarma.objects.all()
    return render_to_response('index.html',{'luces':luces,'puertas':puertas, 'habitaciones':habitaciones, 'sanitarios':sanitarios,'alarmas':alarmas},context)

def luz(request, id_luz):
    context = RequestContext(request)
## Codigo para que prenda y apage la luz
##
    luz = Luz.objects.get(id = id_luz)
    if luz.status:
        luz.status = False
    else:
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
    ## Codigo para que cierra y abra la puerta
    ##
    puerta = Puerta.objects.get(id = id_puerta)
    if puerta.status:
        puerta.status = False
    else:
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
