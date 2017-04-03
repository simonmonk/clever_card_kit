#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    while True:
        id, text = reader.read()
        print(id)
        print(text)

finally:
    print("cleaning up")
    GPIO.cleanup()
