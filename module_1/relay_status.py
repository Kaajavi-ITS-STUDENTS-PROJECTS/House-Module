import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]

def getStatus(pin):
    GPIO.setup(pin, GPIO.IN)
    if GPIO.input(pin):
        return True
    else:
        return False
