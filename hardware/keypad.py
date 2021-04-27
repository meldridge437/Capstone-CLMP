#################################################
#
#	source: https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad
#	Adapted By: Matthew Eldridge
#	Project: Capstone Doorlock
#
#################################################

import adafruit_matrixkeypad
from digitalio import DigitalInOut
import board
from time import sleep

# Classic 4x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.D18, board.D19, board.D20, board.D21)]
rows = [DigitalInOut(x) for x in (board.D22, board.D23, board.D24, board.D25)]
keys = ((1, 2, 3, 'R'),
        (4, 5, 6, 'Y'),
        (7, 8, 9, 'N'),
        ('*', 0, '#', 'E'))
''' letter buttons redefined meanings
R - reset
Y - yes
N - no
E - enter
* - scan finger
# - scan face
'''
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
keyPressed = keypad.pressed_keys

################# Functions #######################

def getPIN(lengthPIN=8):
	pin = []
	strPIN = ""
	while True:
		if(str(keyPressed).isdigit()):
			pin.append(keyPressed)
		if (len(pin) <= lengthPIN or keyPressed == 'E'):
			break	
	for n in pin:
		strPIN += str(n)
	return int(strPIN)

def getLetterResponse():
	while True:
		if (not str(keyPressed).isdigit()):
			return keyPressed
		sleep(0.1)

#################### MAIN #########################
"""
# given sample for testing
while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    sleep(0.1)""""
