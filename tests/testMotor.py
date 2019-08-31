# test motor control chip

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

LOAD_SERVO = 4
FIRING_SERVO = 17
EN1_2_MOTOR = 14
EN3_4_MOTOR = 15

M1_A_MOTOR = 8
M1_B_MOTOR = 7

M2_A_MOTOR = 18
M2_B_MOTOR = 21

GPIO.setup(EN1_2_MOTOR,GPIO.OUT)
GPIO.setup(EN3_4_MOTOR,GPIO.OUT)
GPIO.setup(M1_A_MOTOR,GPIO.OUT)
GPIO.setup(M1_B_MOTOR,GPIO.OUT)
GPIO.setup(M2_A_MOTOR,GPIO.OUT)
GPIO.setup(M2_B_MOTOR,GPIO.OUT)

# noise issue
GPIO.setup(LOAD_SERVO, GPIO.OUT)
GPIO.setup(FIRING_SERVO, GPIO.OUT)

time.sleep(1.0)                   #continues for a half a second

# all motors halted
GPIO.output(EN1_2_MOTOR, False)	
GPIO.output(EN3_4_MOTOR, False)	

GPIO.output(M1_A_MOTOR, False)	
GPIO.output(M1_B_MOTOR, False)	

GPIO.output(M2_A_MOTOR, False)	
GPIO.output(M2_B_MOTOR, False)	

GPIO.output(LOAD_SERVO, False)
GPIO.output(FIRING_SERVO, False)


try:

	# testing the MOTORs

 	# Motor 1 On Counter Clockwise	
	print "Motor 1 on Counter Clockwise"
	GPIO.output(M1_A_MOTOR, False)	
	GPIO.output(M1_B_MOTOR, True)	
 	# Motor 2 On Counter Clockwise	
	print "Motor 2 on Counter Clockwise"
	GPIO.output(M2_A_MOTOR, False)	
	GPIO.output(M2_B_MOTOR, True)	
	# enable Motor 1
	# enable Motor 2
	GPIO.output(EN1_2_MOTOR, True)	
	GPIO.output(EN3_4_MOTOR, True)	

	time.sleep(4.0)
	GPIO.output(EN1_2_MOTOR, False)	
	GPIO.output(EN3_4_MOTOR, False)	

except KeyboardInterrupt:


	GPIO.cleanup()

