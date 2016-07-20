#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        text = raw_input('New Text: ')
        print("Now scan a tag to write")
        tag = reader.write(8, text) 
        
        print("written")
        print(tag['id'])
        print(tag['text'])
finally:
    print("cleaning up")
    GPIO.cleanup()

GPIO.cleanup()