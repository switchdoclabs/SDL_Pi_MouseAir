import RPi.GPIO as GPIO

LOADING_SERVO = 4

import time




def loadMouse():
	print "loadMouse servo"
	servo.start(4.5) 
	time.sleep(1.0)
	servo.stop()


def dropMouse():

	print "dropMouse servo"
	servo.start(10.5) 
	time.sleep(1.0)
	servo.stop()


	
GPIO.setmode(GPIO.BCM)

GPIO.setup(LOADING_SERVO, GPIO.OUT)
servo = GPIO.PWM(LOADING_SERVO, 50) 



loadMouse()

dropMouse()


GPIO.cleanup()
