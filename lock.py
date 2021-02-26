import RPi.GPIO as GPIO
import time
lockPin = 26 #BCM pin number of solenoid
lockTime = 3 #in seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(lockPin, GPIO.OUT)
def unlockTimed():
    GPIO.output(lockPin, GPIO.HIGH)
    time.sleep(lockTime)
    GPIO.output(lockPin, GPIO.LOW)
def unlock():
    GPIO.output(lockPin, GPIO.HIGH)
def lock():
    GPIO.output(lockPin, GPIO.LOW)
