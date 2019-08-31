

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

PAN_SERVO = 11
GPIO.setup(PAN_SERVO,GPIO.OUT)

p = GPIO.PWM(PAN_SERVO,50)        #sets pin 21 to PWM and sends 50 signals per second

p.start(12.5)          #starts by sending a pulse at 7.5% to center the servo

time.sleep(1.0)                   #continues for a half a second

# testing a SG90 Tower Pro 9g Servo
try:


        p.ChangeDutyCycle(2.5)    #sends a 2.5% pulse to turn the servo CCW

        time.sleep(1.0)                   #continues for a half a second

        #p.ChangeDutyCycle(12.0)    #sends a 12.0% pulse to turn the servo CW

        #time.sleep(0.5)                   #continues for a half a second

        #p.ChangeDutyCycle(7.5)    #sends a 7.5% pulse to center the servo again

        #time.sleep(0.5)                   #continues for a half a second

        p.start(12.5)          #starts by sending a pulse at 7.5% to center the servo

        time.sleep(1.0)                   #continues for a half a second
except KeyboardInterrupt:

    p.stop()

    GPIO.cleanup()

