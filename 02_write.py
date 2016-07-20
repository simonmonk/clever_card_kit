#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

text = raw_input('New Text: ')
print("Now scan a tag to write")

tag = reader.write(8, text) 
        
print("written")
print(tag['id'])
print(tag['text'])

GPIO.cleanup()