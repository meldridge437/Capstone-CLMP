import time
import RPi.GPIO as GPIO
from pygame import mixer
import sys
sys.path.append("./hardware")
#test

#hardware modules
from hardware import keypad as keypadMod
from hardware import fingerprint as fprintMod
from hardware import lock as lockMod
from hardware import RGB as rgbMod
#may not set global variable in facial req file
from facial_req import *
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 17
greenPin = 16
bluePin = 13
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

# Initialize pygame mixer
mixer.init()


# Load the sounds
sound = mixer.Sound('applause-1.wav')

enteredPin = ""

def check_fingerprint():
    return fprintMod.get_fingerprint(), fprintMod.finger.finger_id

#init led
rgbMod.lightBlue()
sleep(1)
rgbMod.red()

openLock = False
# If button is pushed, light up LED
try:
    while True:
        rgbMod.red()
        #Check for key entry, when key is in database, check fingerprint and/or facial
        keys = keypadMod.keypad.pressed_keys()
        
        while(keys != "E" and len(enteredPin) < 8):
            if keys:
                enteredPin += keys[0]
            ## Check if in database ##
        dbEntry = findInDB(["username", "fingerID"], ["pin"], [enteredPin])
        #if keypin is valid
        if (dbEntry != []):
            # activate fingerprint sensor
            if keys == "*":
                openLock, fingerID_Actual = check_fingerprint()
                if fingerID_Actual == dbEntry[1] and openLock:
                    #openDoor 2 step MFA
                    rgbMod.green()
                    lockMod.unlockTimed()
            #activate facial req
            if keys == "#":
                while(keys != "E"):
                    #call facial req's main
                    faceDetected, name = main()
                    #make sure same name as matched with key pin
                    if (faceDetected and name == dbEntry[0]):
                        #openDoor 2 step MFA success
                        rgbMod.green()
                        lockMod.unlockTimed()
                        break

# When you press ctrl+c, this will be called
finally:
    cv2.destroyAllWindows()
    vs.stop()
    GPIO.cleanup()

