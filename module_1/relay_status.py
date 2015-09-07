import RPi.GPIO as GPIO

def getStatus(pin):
    GPIO.setmode(GPIO.BCM)
    pinList = [15, 22, 9, 10]
    GPIO.setup(pin, GPIO.IN)
    if GPIO.input(pin):
        return True
    else:
        return False
    GPIO.cleanup()
