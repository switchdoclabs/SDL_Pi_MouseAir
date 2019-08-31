#pi Camera and AI Threads


# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config

import state
import AccessSensors

import requests
import time 
import picamera
import state
import cv2
import traceback
import threading
import os
import sys

import hashlib

import io
import logging
import socketserver

import numpy as np
import datetime as dt

from threading import Condition
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler,HTTPServer

from PIL import ImageFont, ImageDraw, Image


from imutils.video import VideoStream
import imutils
import cv2
import numpy as np
#from tensorflow.python.framework import ops

import AICatNotCat

import updateBlynk

def CatAnalyzeFrame(frame):
    

                # prepare the image to be classified by our deep learning network
                image = cv2.resize(frame, (150, 150))
                image = image.astype("float") / 255.0

                Cat = AICatNotCat.AnalyzeCatNotCat(image)
                #label = str(state.piccount)+"Cat"
                label = "Cat"
                proba = Cat
        
                if (proba> state.CatNotCatThresholdV14):
                    textcolor = (0,0,255)
                else:
                    textcolor = (0,0,0)
        
                # build the label and draw it on the frame
                label = "{}: {:.2f}%".format(label, proba )
        
                # get the width and height of the text box
                font_scale = 1.0
                font = cv2.FONT_HERSHEY_SIMPLEX
                # set the rectangle background to white
                rectangle_bgr = (255, 255, 255)
        
                (text_width, text_height) = cv2.getTextSize(label, font, fontScale=font_scale, thickness=1)[0]
                # set the text start position
                text_offset_x = 10
                #text_offset_y = frame.shape[0] - 25
                text_offset_y =40
                # make the coords of the box with a small padding of two pixels
                box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width - 0, text_offset_y - text_height - 6))
                cv2.rectangle(frame, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
                cv2.putText(frame, label, (text_offset_x, text_offset_y-4), font, fontScale=font_scale, color=textcolor, thickness=3)

                # show the output frame
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF

                # update state
                state.SensorCatNotCatLevel = proba
        
                # now let's set the appropriate variables for detection
             
                if (proba > state.CatNotCatThresholdV14):
                    state.CatDetectedNumberOfFrames = state.CatDetectedNumberOfFrames + 1
                else:
                    state.CatDetectedNumberOfFrames = 0
             
                if (config.DetectCatNumberOfFrames < state.CatDetectedNumberOfFrames):
                    state.CatDetected = True
                else:
                    pass # Note, once we detect the cat, then it is up to the MouseAir launch logic to clear this
               
                # every 10 frames save
                if ((state.piccount % 10) == 0):
                    # delete old photo


                    myHeader = "FlaskServer/static/MouseAir"
                    try:
                        os.remove(myHeader+str(state.piccount-10)+".jpg")
                    except:
                        pass

                    # write frame out for serving
                    cv2.imwrite(myHeader+str(state.piccount)+".jpg", frame)

                state.piccount = state.piccount + 1

