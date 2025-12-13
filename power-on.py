#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.HIGH)

# Turn the power on
GPIO.output(PIN, GPIO.LOW)
time.sleep(0.5)
GPIO.output(PIN, GPIO.HIGH)

GPIO.cleanup()
