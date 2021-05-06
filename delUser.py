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

    #load pickle file
    data=[]
    with (open("encodings.pickle", "rb")) as fr:
        while True:
            try:
                data.append(pickle.load(fr))
            except EOFError:
                break

    # initialize the list of known encodings and known names
    try:
        knownEncodings = data[0]['encodings']
        knownNames = data[0]['names']
    except:
        knownEncodings=[]
        knownNames=[]
    pastName =  False

    # loop over the names
    index = []
    for i in len(knownNames):
        if name == knownNames[i]:
            index.append(i)
    
    for i in len(index):
        del knownNames[index[-1]]
        del knownEncodings[index[-1]]

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f=open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()

    fprintMod.delete_finger(dbEntry[2])

main()