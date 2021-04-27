import RPi.GPIO as GPIO
import time
lockPin = 26 #BCM pin number of solenoid

GPIO.setmode(GPIO.BCM)
GPIO.setup(lockPin, GPIO.OUT)
def unlockTimed(lockTime = 3 ): #in seconds
    GPIO.output(lockPin, GPIO.HIGH)
    time.sleep(lockTime)
    GPIO.output(lockPin, GPIO.LOW)
def unlock():
    GPIO.output(lockPin, GPIO.HIGH)
def lock():
    GPIO.output(lockPin, GPIO.LOW)
