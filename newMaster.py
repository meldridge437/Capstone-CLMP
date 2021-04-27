import time
import RPi.GPIO as GPIO
from pygame import mixer
import sys
sys.path.append("./hardware")

from hardware import keypad as keypadMod
from hardware import fingerprint as fprintMod
from hardware import lock as lockMod
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

def check_fingerprint():
    return fprintMod.get_fingerprint(), fprintMod.finger.finger_id

openLock = False
# If button is pushed, light up LED
try:
    while True:
        current_state = GPIO.input(btn_pin)
        if (current_state == False) and (prev_state == True):
            sound.play()
        prev_state = current_state
        
        #Check for key entry, when key is in database, check fingerprint and/or facial
        keys = keypadMod.keypad.pressed_keys
        
        while(keys != "E" and len(enteredPin) < 8):
            if keys:
                enteredPin += keys[0]
            ## Check if in database ##
        dbEntry = findInDB(["username", "fingerID"], ["pin"], [enteredPin])
        if (dbEntry != []):
            # do things
            if keys == "*":
                openLock, fingerID_Actual = check_fingerprint()
                if fingerID_Actual == dbEntry[1] and openLock:
                    lockMod.unlock()





# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

