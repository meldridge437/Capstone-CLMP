import RPi.GPIO as GPIO
from time import sleep

LED = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def turnOn():
    GPIO.output(LED, GPIO.HIGH)
    sleep(4)
    
def turnOff():    
    GPIO.output(LED, GPIO.LOW)
    sleep(4)


turnOn()
turnOff()
turnOn()
turnOff()

GPIO.cleanup()
