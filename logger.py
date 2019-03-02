# run cmd -m pip install pynput
import pynput

from pynput.keyboard import Key, Listener


def on_press(key):
    #log into console what keys are pressed
    print("(0) pressed".format(key))

def on_release(key):
    #break out fo the program when the Escape key is pressed
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
