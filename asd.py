#!/usr/bin/python
import RPi.GPIO as GPIO
import time
PRENDIDO = GPIO.LOW
APAGADO = GPIO.HIGH
GPIO.setmode(GPIO.BCM)
# init list with pin numbers
pinList = [15, 22, 9, 10]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, APAGADO)
SleepTimeL = 2
# main loop
try:
    time.sleep(SleepTimeL);
    GPIO.output(15, PRENDIDO)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, PRENDIDO)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, PRENDIDO)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, PRENDIDO)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.cleanup()
    print "Good bye!"
    # End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
