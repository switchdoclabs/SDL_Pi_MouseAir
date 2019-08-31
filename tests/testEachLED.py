

print "started"
import RPi.GPIO as GPIO 
print "after import"

import time
print "after time import"

GPIO.setmode(GPIO.BCM)

LOAD_SERVO = 4
FIRE_SERVO = 17

EN1_MOTOR = 14
EN2_MOTOR = 15

GPIO.setup(LOAD_SERVO,GPIO.OUT)
GPIO.setup(FIRE_SERVO,GPIO.OUT)
GPIO.setup(EN1_MOTOR,GPIO.OUT)
GPIO.setup(EN2_MOTOR,GPIO.OUT)


time.sleep(1.0)                   #continues for a half a second

try:

	while True:
	
        	GPIO.output(LOAD_SERVO, True)
		time.sleep(1.0) 
        	GPIO.output(LOAD_SERVO, False)
        	time.sleep(1.0)                   #continues for a half a second

        	GPIO.output(FIRE_SERVO, True)
		time.sleep(1.0) 
        	GPIO.output(FIRE_SERVO, False)
        	time.sleep(1.0)                   #continues for a half a second

        	GPIO.output(EN1_MOTOR, True)
		time.sleep(1.0) 
        	GPIO.output(EN1_MOTOR, False)
        	time.sleep(1.0)                   #continues for a half a second

        	GPIO.output(EN2_MOTOR, True)
		time.sleep(1.0) 
        	GPIO.output(EN2_MOTOR, False)
        	time.sleep(1.0)                   #continues for a half a second




except KeyboardInterrupt:

	GPIO.cleanup()

