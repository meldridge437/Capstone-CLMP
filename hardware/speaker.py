from time import sleep, time
import RPi.GPIO as GPIO
import contextlib
with contextlib.redirect_stdout(None):

    from pygame import mixer
from array import array

# Initialize pygame mixer
mixer.init()

# Load the sounds
goodSound = mixer.Sound('applause-1.wav')
badSound = mixer.Sound('bad.wav')

def success():

    goodSound.play()
    sleep(4)
    goodSound.stop() 
def fail():
    badSound.play()
    sleep(3)
    badSound.stop()
