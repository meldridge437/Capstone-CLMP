import time
import RPi.GPIO as GPIO
from pygame import mixer
import sys
sys.path.append("./hardware")

from hardware import keypad as keypadMod

# Pins definitions
btn_pin = 22

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)

# Initialize pygame mixer
mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True

# Load the sounds
sound = mixer.Sound('applause-1.wav')


enteredPin = ""


# If button is pushed, light up LED
try:
    while True:
        current_state = GPIO.input(btn_pin)
        if (current_state == False) and (prev_state == True):
            sound.play()
        prev_state = current_state
        
        #Check for key entry, when key is in database, check fingerprint and/or facial
        keys = keypadMod.keypad.pressed_keys
        
        while(keys != "E"):
            if keys:
                enteredPin += keys
            ## Check if in database ##
            ## To Do ##

            #if in database


# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

