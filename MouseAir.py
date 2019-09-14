#!/usr/bin/python
# MouseAir Controller Program
# SwitchDoc Labs July 2019
#
# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config


import logging

import threading
import traceback
import state

from neopixel import *
import pixelDriver


config.SWVERSION = "V011"


import SensorThreads

import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

sys.path.append('./FlaskServer')
import FlaskServer


import subprocess

from datetime import datetime

import random 
import re
import math
import os

import sendemail

import utils

import Motors 
import MouseDetector

import AICatNotCat
import CameraThreads

import LaunchJob 
from PIL import Image

import updateBlynk
import imutils


from imutils.video import VideoStream

from apscheduler.schedulers.background import BackgroundScheduler

import apscheduler.events


GPIO.setmode(GPIO.BCM)



if (config.USEBLYNK):
     updateBlynk.blynkInit()
            


if (config.USEBLYNK):
     updateBlynk.blynkStatusTerminalUpdate("SW Startup Version "+config.SWVERSION) 

subjectText = "MouseAir Raspberry Pi has #rebooted."
ipAddress = subprocess.check_output(['/bin/hostname', '-I'])

splitipAddress = ipAddress.split()
ipAddress = splitipAddress[0]
state.LocalIPAddress = ipAddress.decode('UTF-8')
state.LocalIPAddress = state.LocalIPAddress.rstrip()
#ipAddress = subprocess.check_output('/bin/hostname -I')
print("ip=",state.LocalIPAddress)


bodyText = "MouseAir Version "+config.SWVERSION+ " Startup \n"+ipAddress.decode('UTF-8')+"\n"
sendemail.sendEmail("test", bodyText, subjectText ,config.notifyAddress,  config.fromAddress, "");


# read and set State Variables

def readState():
    pass

def writeState():
    pass





# print out faults inside events
def ap_my_listener(event):
        if event.exception:
              print (event.exception)
              print (event.traceback)

# apscheduler events

def tick():
    print('Tick! The time is: %s' % datetime.now())


def killLogger():
    scheduler.shutdown()
    print ("Scheduler Shutdown....")


def checkForButtons():
    # see if buttons need updates or actions
    
    updateBlynk.blynkStatusUpdate()






# main Program

logging.basicConfig(format="%(module)s: %(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
module_logger = logging.getLogger('MouseAir')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
format = logging.Formatter("MouseAir:%(asctime)s: %(message)s")
ch.setFormatter(format)
module_logger.addHandler(ch)

module_logger.info("MouseAir Version "+config.SWVERSION)
print("MouseAir Version "+config.SWVERSION)

state.strip = Adafruit_NeoPixel(pixelDriver.LED_COUNT, pixelDriver.LED_PIN, pixelDriver.LED_FREQ_HZ, pixelDriver.LED_DMA, pixelDriver.LED_INVERT, pixelDriver.LED_BRIGHTNESS, pixelDriver.LED_CHANNEL, pixelDriver.LED_STRIP)

state.strip.begin()
pixelDriver.setStripBrightness()

state.PixelLock = threading.Lock()
# Set up scheduler

scheduler = BackgroundScheduler()
logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)

# for debugging
scheduler.add_listener(ap_my_listener, apscheduler.events.EVENT_JOB_ERROR)

##############
# setup tasks
##############

# prints out the date and time to console
scheduler.add_job(tick, 'interval', seconds=60)


# every minute, check for button changes
scheduler.add_job(checkForButtons, 'interval', seconds=5)   

scheduler.add_job(updateBlynk.blynkStateUpdate, 'interval', seconds=5)   

scheduler.add_job(updateBlynk.blynkUpdateImage, 'interval', seconds=1)   

scheduler.add_job(LaunchJob.checkForLaunch, 'interval', seconds=5)   


# blink optional life light

    
scheduler.add_job(pixelDriver.blinkLED, 'interval', seconds=2.5, args=[0,1,0.250])

# Status lights
scheduler.add_job(pixelDriver.statusLEDs, 'interval', seconds=3.2, args=[])


# start scheduler
scheduler.start()
print("-----------------")
print("Scheduled Jobs")
print("-----------------")
scheduler.print_jobs()
print("-----------------")


# start Sensor Threads


T1 = threading.Thread(target=SensorThreads.readUltrasonicSensor,args=())
T1.start()
T2 = threading.Thread(target=SensorThreads.readMouseDetect,args=())
T2.start()

# start Flask Thread

T3 = threading.Thread(target=FlaskServer.threadFlask,args=((False,)))
T3.start()

# test Launch
#launchMouse()

# the main loop

logging.info("MouseAir Main Loop")

try:


    # initialize the video stream and allow the camera sensor to warm up
    
    print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    vs.camera.rotation=180
    # loop over the frames from the video stream
    
    while True:
        
	# grab the frame from the threaded video stream and resize it
        # to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=500)
        
        CameraThreads.CatAnalyzeFrame(frame)

        


except:

    print("exiting MouseAir")
    traceback.print_exc()
    killLogger()


