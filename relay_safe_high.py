#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal
import sys

RELAY_PIN = 17

def cleanup(*_):
    try:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Just in case OFF
        GPIO.cleanup()
    finally:
        sys.exit(0)

signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

GPIO.setmode(GPIO.BCM)

# Set HIGH（=Relay OFF）
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Continue to keep by systemd
while True:
    time.sleep(3600)
