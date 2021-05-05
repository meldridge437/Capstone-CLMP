from time import sleep
import RPi.GPIO as GPIO
#from pygame import mixer
import sys
sys.path.append("./hardware")
#test
sys.path.append("./test/facial_recognition")

sys.path.append("./facetest")
#hardware modules
from hardware import keypad as keypadMod
from hardware import fingerprint as fprintMod
from hardware import lock as lockMod
from hardware import RGB as rgbMod
import db_client as db


#may not set global variable in facial req file

from facetest import facial_req as fq
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 17
greenPin = 16
bluePin = 12
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
#lock time variable
lockTime=3

# Initialize pygame mixer
#mixer.init()


# Load the sounds
#sound = mixer.Sound('applause-1.wav')

enteredPin = ""

def check_fingerprint():
    return fprintMod.get_fingerprint(), fprintMod.finger.finger_id

#init led
rgbMod.lightBlue()
sleep(1)
rgbMod.red()

#init lock
lockMod.lock()

openLock = False
# If button is pushed, light up LED
try:
    while True:
        print("Awaiting KeyPad Entry...")
        rgbMod.red()
        #Check for key entry, when key is in database, check fingerprint and/or facial
        keys = keypadMod.keypad.pressed_keys
        
        while(keys != ['E'] and len(enteredPin) < 8):
            keys = keypadMod.keypad.pressed_keys
            if keys:
                print(keys[0])
                enteredPin += str(keys[0])
                sleep(.5)
          
          ## Check if in database ##
        try:
            dbEntry = db.findInDB(["username", "fingerID"], ["pin"], [enteredPin])
            print("keypad correct")
            valid_key = True
        except:
            print("keypad incorrect")
            valid_key = False
            pass 
        
        print("Press * for Fingerprint Scanning")
        print("Press # for Facial Recognition")
        while(True):
            rgbMod.blue()
            openLock = False
            fingerID_Actual = 0
            keys = keypadMod.keypad.pressed_keys
            if keys:

                # activate fingerprint sensor
                if keys[0] == "*":
                    openLock, fingerID_Actual = check_fingerprint()
                    if valid_key:
                        
                        if openLock and fingerID_Actual == dbEntry[1]:
                            #openDoor 2 step MFA
                            rgbMod.green()
                            lockMod.unlockTimed(lockTime)
                        else:
                            enteredPin = ""
                        break
                    else:
                        enteredPin = ""
                        break
                #activate facial req
                elif keys[0] == "#":
                    while(keys != "E"):
                        #call facial req's main
                        faceDetected, name = fq.main()
                        #make sure same name as matched with key pin
                        if (faceDetected and name == dbEntry[0]):
			#openDoor 2 step MFA success
                            rgbMod.green()
                            lockMod.unlockTimed(lockTime)
                            enteredPin = ""
                            break
                        else:
                            enteredPin = ""
                            break


                    break

# When you press ctrl+c, this will be called
finally:
    fq.cv2.destroyAllWindows()
    fq.vs.stop()
    GPIO.cleanup()

