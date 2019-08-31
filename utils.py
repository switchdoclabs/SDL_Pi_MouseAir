
from threading import Thread
import sys
import time
import datetime

import subprocess


# Takes a single picture on System 
# filename: takeSinglePicture.py
# Version 1.0  10/31/13
#
# takes a picture using the camera 
#
#



def  takePicture(source):

        try:
                f = open("/home/pi/MouseAir/state/exposure.txt", "r")
                tempString = f.read()
                f.close()
                lowername = tempString

        except IOError as e:
                 lowername = "auto"

        exposuremode = lowername
	# take picture
        print("taking picture")
        cameracommand = "raspistill -o /home/pi/RasPiConnectServer/static/picameraraw.jpg -t 750 -ex " + exposuremode
        print(cameracommand)
        output = subprocess.check_output (cameracommand,shell=True, stderr=subprocess.STDOUT )
        print("adding tag to picture")
        output = subprocess.check_output("convert '/home/pi/RasPiConnectServer/static/picameraraw.jpg' -pointsize 72 -fill white -gravity SouthWest -annotate +50+100 'Mouse Air %[exif:DateTimeOriginal]' '/home/pi/RasPiConnectServer/static/picamera.jpg'", shell=True, stderr=subprocess.STDOUT)


        print("Thread ending. finished taking picture")
        return

# thread camera

def threadTakePicture(source):

	
        cameraThread = Thread(target=takePicture, args=(source,))
        cameraThread.daemon = True
        cameraThread.start()	
        print("camera Thread Starting")
        return

