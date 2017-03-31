#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        text = raw_input('New Text: ')
        sector = raw_input('Sector: ')
        print("Now scan a tag to write")
        tag = reader.write(text, sector) 
        
        print("written")
        print(tag['id'])
        print(tag['text'])
finally:
    print("cleaning up")
    GPIO.cleanup()