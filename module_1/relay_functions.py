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
        return False
    else:
        return True

def dance():
    SleepTimeL = 0.2
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
    time.sleep(0.1);
    GPIO.output(15, OFF)
    print "ONE"
    time.sleep(0.1);
    GPIO.output(22, OFF)
    print "FOUR"
    time.sleep(0.1);
    GPIO.output(9,OFF)
    print "FOUR"
    time.sleep(0.1);
    GPIO.output(10,OFF)
    print "Good bye!"
