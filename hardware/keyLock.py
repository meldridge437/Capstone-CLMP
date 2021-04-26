#!/usr/bin/env python

from pynput import keyboard
import lock
state=0

def on_press(key):
    global state
    if key==keyboard.Key.enter:
        if state==1:
            state=0
            lock.unlock()
        else:
            state=1
            lock.lock()
    if key==keyboard.Key.esc:
        return False

listener=keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
