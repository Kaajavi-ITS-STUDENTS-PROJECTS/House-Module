#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# loop through pins and set mode and state to 'low'
SleepTimeL = 2
    # main loop
try:
    GPIO.output(15, GPIO.LOW)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, GPIO.LOW)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, GPIO.LOW)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, GPIO.LOW)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.cleanup()
    print "Good bye!"
    # End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
