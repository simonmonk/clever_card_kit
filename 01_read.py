#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    while True:
        tag = reader.read()
        print(tag['id'])
        print(tag['text'])

finally:
    print("cleaning up")
    GPIO.cleanup()
