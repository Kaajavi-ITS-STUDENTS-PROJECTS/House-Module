#!/usr/bin/python
import RPi.GPIO as GPIO
# reinvertir la programacion
ON = GPIO.LOW
OFF = GPIO.HIGH


def setting_pines():
    print("Settings pinout")
    # init de los pins
    GPIO.setmode(GPIO.BCM)
    pinList = [15, 22, 9, 10]
    GPIO.setup(pinList, GPIO.OUT, initial=OFF)
    GPIO.setup(pinList, GPIO.IN)

def relay(do, pin):
    GPIO.setup(pin, GPIO.OUT)
    print(do)
    if do=="open":
        GPIO.output(pin, ON)
    else:
        GPIO.output(pin, OFF)

def getStatus(pin):
    GPIO.setup(pin, GPIO.IN)
    if GPIO.input(pin):
        return True
    else:
        return False
