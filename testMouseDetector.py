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

import MouseDetector
import traceback

print ("")
print ("Test Mouse Presence Detector Version 1.0 - SwitchDoc Labs")
print ("")
print ("Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S"))
print ("")

MouseDetector.SetupMouseDetector()



try:
    while (True):

        if (MouseDetector.CheckMousePresent() == 0):
            print ('Mouse Detected') 
        else: 
            print ('Mouse NOT Detected') 
        time.sleep(0.3)

except:
    print(traceback.format_exc())
    GPIO.cleanup()
