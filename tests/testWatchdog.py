

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

RELAY_ON = 18
DOG1_OUT = 23
GPIO.setup(DOG1_OUT,GPIO.IN)
GPIO.setup(RELAY_ON,GPIO.IN)

try:

	myTrigger = False
	myTriggerTime = 0
	while True:
	# testing the Relay 
	
		print "pulse"	
		GPIO.setup(RELAY_ON,GPIO.OUT)
        	GPIO.output(RELAY_ON, False)
        	time.sleep(2.5)                   #continues for a half a second
		GPIO.setup(RELAY_ON,GPIO.IN)
		print "pulsedone"	
		time.sleep(1);

		for i in range(0, 240):
			time.sleep(0.25)
    			print "Time= %3.2f" % (i/4.0)
			if (GPIO.input(DOG1_OUT) == 1):
				myTrigger = True
				myTriggerTime = i/4.0
				print "-------------->Trigger"

except KeyboardInterrupt:

	print "myTrigger = ",  myTrigger
	print "myTriggerTime = ",  myTriggerTime
	GPIO.cleanup()

