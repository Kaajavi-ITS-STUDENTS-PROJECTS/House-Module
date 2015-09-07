import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pinList = [15, 22, 9, 10]

for i in pinList:
    GPIO.setup(i, GPIO.IN)

def getStatus(pin):
    if GPIO.input(pin):
        return True
    else:
        return False
    GPIO.cleanup()
