#!/usr/bin/env python
#
#
# SwitchDoc Labs, July 2019
#

# imports

import sys
import time
import datetime
import random 
import Motors
import traceback

print ""
print "Test Launch Motors Version 1.0 - SwitchDoc Labs"
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

print('moving motor')
try:
    while True:

        Motors.launchMotorsOn()
        time.sleep(2.3)
        Motors.launchMotorsOff()
        time.sleep(2.3)


except:
    print(traceback.format_exc())
    print('shutting down motors')
    Motors.launchMotorsOff()

