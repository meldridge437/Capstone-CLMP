from time import sleep
import RPi.GPIO as GPIO
import sys
from random import randint
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
    passcode = 0
    #generate passcode
    while True:
        for i in range(4):
           digit = randint(0,9)
           if i == 0:
               passcode=digit
            else:
                passcode = str(passcode) + str(digit)
        dbEntry = db.findInDB(["id"], ["pin"], [db.hashPin(passcode)])
        if dbEntry == []:
            print("Passcode is {}".format(passcode))
            break

    #generate fingerID
    finger = 1
    while True:
        dbEntry = db.findInDB(["id"], ["fingerID"], [finger])
        if dbEntry == []:
            break
        finger += 1
    fprintMod.enroll_finger(finger)

    #generate face files
    while True:
        print("Enter Name: ")
        name=input()
        if name == "":
            continue
        else:
            break
    face.addPic(name)

    #add to Database
    db.createNewDBEntry(["username", "pin", "fingerID"], [name, db.hashPin(passcode), finger])
    print("User {} added".format(name))

main()