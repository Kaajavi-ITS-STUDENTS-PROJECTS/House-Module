#!/usr/bin/python
import RPi.GPIO as GPIO

# reinvertir la programacion
ON = GPIO.LOW
OFF = GPIO.HIGH

# init de los pins
GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]
for i in pinList:
    GPIO.setup(i, GPIO.IN)
    GPIO.input(i)
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, OFF)

def relay(do, pin):
    if do=="open":
        GPIO.output(pin, ON)
    else:
        GPIO.output(pin, OFF)

def getStatus(pin):
    if GPIO.input(pin):
        return True
    else:
        return False
