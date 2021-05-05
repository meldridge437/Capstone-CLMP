from time import sleep
import RPi.GPIO as GPIO
import sys
from random import randint
from shutil import rmtree
sys.path.append("./hardware")
sys.path.append("./facetest")

#hardware modules
from hardware import keypad as keypadMod
from hardware import fingerprint as fprintMod
from hardware import RGB as rgbMod
from hardware import speaker as speak
import db_client as db
from facetest import headshotsModule as face

def main():
    enteredPin = ""
    while True:
        print("Awaiting KeyPad Entry...")
        #Check for key entry, when key is in database, check fingerprint and/or facial
        keys = keypadMod.keypad.pressed_keys
        
        while(keys != ['E'] and len(enteredPin) < 4):
            keys = keypadMod.keypad.pressed_keys
            if keys:
                print(keys[0])
                enteredPin += str(keys[0])
                sleep(.5)
        
        ## Check if in database ##
        try:
            dbentry = db.findInDB(["id","username", "fingerID"], ["pin"], [db.hashPin(enteredPin)])
            print("keypad correct")
            valid_key = True
            break
        except:
            print("keypad incorrect")
            valid_key = False
    db.deleteDBEntry(dbEntry[0])
    try:
        rmtree("facetest/dataset/"+dbEntry[1])
    except:
        print("Could not find {}".format(dbEntry[1]))
    fprintMod.delete_finger(dbEntry[2])
