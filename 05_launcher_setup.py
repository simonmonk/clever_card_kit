#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import os
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


def add_command(id, command):
    global tags
    tags[id] = command
    save_tags()
        
load_tags()
        
try:
    while True:
        command = raw_input("Enter command to be run:")
        print("Hold a tag next to the reader")
        id = reader.read_id()
        
        add_command(id, command)
        
finally:
    print("cleaning up")
    GPIO.cleanup()
