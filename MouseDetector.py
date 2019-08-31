#!/usr/bin/env python
#
#
# SwitchDoc Labs, August 2019
#
import RPi.GPIO as GPIO
import sys
import time

# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def SetupMouseDetector():
    GPIO.setup(config.MouseDetectionPin, GPIO.IN)


def CheckMousePresent():

    MousePresent = GPIO.input(config.MouseDetectionPin) 
    return MousePresent
