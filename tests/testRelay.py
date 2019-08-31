

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

RELAY_ON = 18

GPIO.setup(RELAY_ON,GPIO.OUT)


time.sleep(1.0)                   #continues for a half a second

try:

	while True:
	# testing the Relay 
	
        	GPIO.output(RELAY_ON, True)
       	 
		time.sleep(5.0) 
	
        	GPIO.output(RELAY_ON, False)
	
        	time.sleep(4.0)                   #continues for a half a second
except KeyboardInterrupt:

	GPIO.cleanup()

