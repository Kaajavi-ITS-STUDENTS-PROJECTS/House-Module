#!/usr/bin/python
#import RPi.GPIO as GPIO
import time

# reinvertir la programacion
#ON = GPIO.LOW
#OFF = GPIO.HIGH

# init de los pins
#GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]
#for i in pinList:
   # GPIO.setup(i, GPIO.OUT)
    #GPIO.output(i, OFF)

# do abre o cierra dependiendo
def puerta(do, pin):
    pass

def luz(do, pin):
    pass

def getStatus(pin):
    #Devolver el estatus del pin pedido
    return False

'''
import RPi.GPIO as GPIO
import time

# reinvertir la programacion
ON = GPIO.LOW
OFF = GPIO.HIGH

# init de los pins
GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, OFF)

# do abre o cierra dependiendo
def puerta(do, pin):
    if do=="open":
        GPIO.output(pin, ON)
    else:
        GPIO.output(pin, OFF)

def luz(do, pin):
    if do=="open":
        GPIO.output(pin, ON)
    else:
        GPIO.output(pin, OFF)

def getStatus(pin):
    #Devolver el estatus del pin pedido
    return False
'''