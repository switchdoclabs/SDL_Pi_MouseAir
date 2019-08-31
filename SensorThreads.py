# Threads for MosueAir Sensors

import random
import state
import time
import UltraRanger
import MouseDetector

import logging

import RPi.GPIO as GPIO


def readUltrasonicSensor():
    
    
    logging.info("starting readUltrasonicSensor Thread")
    oldValue = 600.0
    while True:
        newValue = UltraRanger.measurementInCM()
        if (newValue == -1):
            newValue = oldValue
        else:
            oldValue = newValue

        
        state.SensorUltrasonicDistance = newValue

        #val = "SensorUltrasonicDistance = ", state.SensorUltrasonicDistance
        #logging.info(val)
        time.sleep(0.2)


def readMouseDetect():
   
    logging.info("starting readMouseDetect Thread")
    MouseDetector.SetupMouseDetector()
    while True:
        if (MouseDetector.CheckMousePresent() == 0):
            state.SensorMouseDetect = 1
        else: 
            state.SensorMouseDetect = 0

        #val = "SensorMouseDetect = ", state.SensorMouseDetect
        #logging.info(val)
        time.sleep(0.2)

