# MouseAir V3 Launch Sequence


import RPi.GPIO as GPIO

import time
import signal

LOAD_SERVO = 4
FIRING_SERVO = 17
EN1_2_MOTOR = 14
EN3_4_MOTOR = 15

M1_A_MOTOR = 8
M1_B_MOTOR = 7

M2_A_MOTOR = 18
M2_B_MOTOR = 21

GPIO.setmode(GPIO.BCM)

def loadMouse(servo):
        print "loadMouse servo"
        servo.start(4.5)
        time.sleep(1.0)
        servo.stop()


def dropMouse(servo):

        print "dropMouse servo"
        servo.start(10.5)
        time.sleep(1.0)
        servo.stop()




time.sleep(1.0)                   #continues for a half a second

try:
	time.sleep(5.0)


	GPIO.setup(LOAD_SERVO, GPIO.OUT)
  
	servo = GPIO.PWM(LOAD_SERVO, 50)
  
    

	loadMouse(servo)
  
	dropMouse(servo)



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

	time.sleep(2.0)
	GPIO.setup(FIRING_SERVO, GPIO.OUT)
	servo = GPIO.PWM(FIRING_SERVO, 50) 

	print "Forward servo"
	servo.start(6.0) 
	time.sleep(0.55)
	servo.stop()


	print "Back servo"
	servo.start(10.5) 
	time.sleep(0.4)
	servo.stop()

	time.sleep(4.0)
	GPIO.output(EN1_2_MOTOR, False)	
	GPIO.output(EN3_4_MOTOR, False)	



	time.sleep(1.0)
	print "ending firing"


	GPIO.cleanup()



except KeyboardInterrupt:

	GPIO.cleanup()

