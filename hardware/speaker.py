import time
import RPi.GPIO as GPIO
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Load the sounds
sound = mixer.Sound('applause-1.wav')

# If button is pushed, light up LED
def playApplause():
    sound.play()
finally:
    GPIO.cleanup()
