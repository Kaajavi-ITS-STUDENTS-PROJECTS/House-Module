#!/usr/bin/python
#import RPi.GPIO as GPIO
#import time

# reinvertir la programacion
#ON = GPIO.LOW
#OFF = GPIO.HIGH

# init de los pins
#GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]
#for i in pinList:
    #GPIO.setup(i, GPIO.OUT)
    #GPIO.output(i, OFF)

# do abre o cierra dependiendo
def puerta(do):pass
    #if do=="open":
     #   GPIO.output(15, ON)
    #else:
      #  GPIO.output(15, OFF)

def luz(do, pin):pass
    #if do=="open":
       # GPIO.output(pin, ON)
    #else:
        #GPIO.output(pin, OFF)

def getStatus(pin):
    return False

#def luz_2(do):
#    if do=="open":
#        GPIO.output(9, ON)
#    else:
#        GPIO.output(9, OFF)
#
#def luz_3(do):
#    if do=="open":
#        GPIO.output(10, ON)
#    else:
#        GPIO.output(10, OFF)
#