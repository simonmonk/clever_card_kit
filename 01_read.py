#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    while True:
        sector = raw_input('Sector: ')
        tag = reader.read(sector)
        print(tag['id'])
        print(tag['text'])

finally:
    print("cleaning up")
    GPIO.cleanup()
