from time import sleep
import RPi.GPIO as GPIO
redPin = 6
greenPin = 5
bluePin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setwarnings(False)
sleep(2)

def turnOff():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def white():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def red():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)

def green():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def blue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def yellow():
    GPIO.output(redPin,GPIO.HGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def purple():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def lightBlue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

