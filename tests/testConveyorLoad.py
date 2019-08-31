# MouseAir V2 Conveyor Load Tests 


import RPi.GPIO as GPIO

import time
import signal

LOAD_SERVO = 4
GPIO.setmode(GPIO.BCM)



time.sleep(1.0)                   #continues for a half a second

try:
	time.sleep(5.0)


	GPIO.setup(LOAD_SERVO, GPIO.OUT)
  
	servo = GPIO.PWM(LOAD_SERVO, 50)
  
    



	# noise issue
	GPIO.setup(LOAD_SERVO, GPIO.OUT)
	time.sleep(1.0)                   #continues for a half a second

	GPIO.setup(LOAD_SERVO, GPIO.OUT)
	servo = GPIO.PWM(LOAD_SERVO, 50) 

	print "load servo"
	servo.start(6.0) 
	time.sleep(0.55)
	servo.stop()


	print "unload servo"
	servo.start(10.5) 
	time.sleep(0.4)
	servo.stop()

	time.sleep(4.0)



	time.sleep(1.0)
	print "ending loading"


	GPIO.cleanup()



except KeyboardInterrupt:

	GPIO.cleanup()

