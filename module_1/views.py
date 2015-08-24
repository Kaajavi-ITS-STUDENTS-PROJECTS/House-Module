from django.shortcuts import render_to_response, render
from django.template import RequestContext
import RPi.GPIO as GPIO
import time
PRENDIDO = GPIO.LOW
APAGADO = GPIO.HIGH

# init de los pins
GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, APAGADO)

# Create your views here.

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
prendido = False

def abrirPuerta(request):
    if prendido==False:
        GPIO.output(15, PRENDIDO)
        prendido = True
    else:
        GPIO.output(15, APAGADO)
        prendido = False

    return render_to_response('index.html',
                             context)
