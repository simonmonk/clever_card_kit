#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import os

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a thing next to the reader")

def speak(message):
    os.system('echo ' + message + ' | festival --tts')

try:
    while True:
        speak('Hold a thing next to the reader')
        id, text = reader.read()
        print(text)
        speak(text)

finally:
    print("cleaning up")
    GPIO.cleanup()
