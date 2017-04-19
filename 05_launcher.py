#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import os, pickle, time
import pickle

reader = SimpleMFRC522.SimpleMFRC522()

tags = {}

def load_tags():
    global tags
    try:
        with open('command_tags.pickle', 'rb') as handle:
            tags = pickle.load(handle)
        print("Loaded Tags")
        print(tags)      
    except:
        pass
    
def save_tags():
    global tags
    print("Saving Tags")
    print(tags)
    with open('command_tags.pickle', 'wb') as handle:
        pickle.dump(tags, handle)
        
load_tags()        

try:
    while True:
        
        print("Hold a tag next to the reader")
        id = reader.read_id()
        command = tags.get(id, None)
        if command:
            print(command)
            os.system(command)
            time.sleep(2) # prevent too many repeats

finally:
    print("cleaning up")
    GPIO.cleanup()
