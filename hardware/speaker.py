from time import sleep, time
import RPi.GPIO as GPIO
import contextlib
with contextlib.redirect_stdout(None):

    from pygame import mixer
from array import array

# Initialize pygame mixer
mixer.init()

# Load the sounds
sound = mixer.Sound('applause-1.wav')
elapsed = time()
def main():

    sound.play()
    sleep(4)
    sound.stop() 
