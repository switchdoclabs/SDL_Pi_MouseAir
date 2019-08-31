#!/usr/bin/env python
#
#
# SwitchDoc Labs, July 2019
#

# imports

import sys
import time
import datetime
import random 


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


print ""
print "Test Launch Motors Version 1.0 - SwitchDoc Labs"
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""
#PC9685 - TB6612FNG
# PWM8  - PWMA
# PWM9  - AIN1
# PWM10 - AIN2
#
# PWM11 - BIN1
# PWM12 - BIN2
# PWM13 - PWMB

pwmA = 8
ain1 = 9
ain2 = 10


pwmB = 11
bin1 = 12
bin2 = 13

servo_speed = 2000
servo_max = 4095

print('moving motor')
try:
    while True:

        pwm.set_pwm(pwmB, 0, servo_speed)
        pwm.set_pwm(bin1, 0, 0)
        pwm.set_pwm(bin2, 0, servo_max)
        time.sleep(2.3)
        pwm.set_pwm(pwmA, 0, servo_speed)
        pwm.set_pwm(bin1, 0, 0)
        pwm.set_pwm(bin2, 0, 0)
        time.sleep(2.3)

except:
    print('shutting down motors')
    pwm.set_pwm(pwmA, 0, 0)
    pwm.set_pwm(pwmB, 0, 0)
    pwm.set_pwm(ain1, 0, 0)
    pwm.set_pwm(ain2, 0, 0)
    pwm.set_pwm(bin1, 0, 0)
    pwm.set_pwm(bin2, 0, 0)
    pwm = PCA9685.PCA9685(address=0x41)

