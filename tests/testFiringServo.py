import RPi.GPIO as GPIO

FIRING_SERVO = 17

import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(FIRING_SERVO, GPIO.OUT)
servo = GPIO.PWM(FIRING_SERVO, 50) 

time.sleep(2.0)
while True:
	print "Forward servo"
	servo.start(6.0) 
	time.sleep(0.55)
	servo.stop()

	time.sleep(1.0)

	servo = GPIO.PWM(FIRING_SERVO, 50) 
	print "Back servo"
	servo.start(10.5) 
	time.sleep(0.55)
	servo.stop()

	time.sleep(1.0)
	print "ending firing"


GPIO.cleanup()
