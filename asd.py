#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# init list with pin numbers
pinList = [22, 15, 13, 16]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    if i<2:
        GPIO.output(22, GPIO.LOW)
    else:
        GPIO.output(22, GPIO.HIGH)
    # time to sleep between operations in the main loop
SleepTimeL = 2
    # main loop
try:
    GPIO.output(22, GPIO.LOW)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(15, GPIO.LOW)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(13, GPIO.LOW)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(16, GPIO.LOW)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.cleanup()
    print "Good bye!"
    # End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
