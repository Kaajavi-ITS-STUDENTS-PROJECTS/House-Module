#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# main loop
ON = GPIO.LOW
OFF = GPIO.HIGH
GPIO.setmode(GPIO.BCM)
# init list with pin numbers
pinList = [15, 22, 9, 10]
# loop through pins and set mode and state to 'low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, OFF)
SleepTimeL = 0.2

try:
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(10, OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(22,OFF)
    time.sleep(SleepTimeL);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(10,OFF)
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(10,OFF)
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(10, OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(22,OFF)
    time.sleep(SleepTimeL);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(SleepTimeL);
    GPIO.output(10,OFF)
    time.sleep(SleepTimeL);
    GPIO.output(15, ON)
    print "ONE"
    time.sleep(SleepTimeL);
    GPIO.output(22, ON)
    print "TWO"
    time.sleep(SleepTimeL);
    GPIO.output(9, ON)
    print "THREE"
    time.sleep(SleepTimeL);
    GPIO.output(10, ON)
    print "FOUR"
    time.sleep(0.05);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(0.05);
    GPIO.output(22, OFF)
    print "FOUR"
    time.sleep(0.05);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(0.05);
    GPIO.output(10,OFF)
    GPIO.cleanup()
    print "Good bye!"
    # End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
