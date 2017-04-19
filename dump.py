#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

blocks = [8, 9, 10, 11]

print("Hold a tag near the reader")

try:
    while True:
        for b in blocks:
            id, text = reader.read(b)
            print("block" + str(b) + ":" + text)

finally:
    print("cleaning up")
    GPIO.cleanup()
