#!/usr/bin/env python
#
#
# Motors Programming 
# 
#
#
#

# imports
from __future__ import division

import sys
import time
import datetime
import random 

import state

sys.path.append('./PCA9685Driver')
# Import the PCA9685 module.
from pca9685_driver import Device

# launch servo
pwm = Device(0x41)
# Set frequency to 60hz, good for pwm.
pwm.set_pwm_frequency(60)

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

servo_max = 4095


# launch motors


def getStatistics():
    return (0,0)

def setLaunchSpeed(Right, Left):
    state.LaunchSpeedRight = Right
    state.LaunchSpeedLeft = Left

def launchMotorsOn(): 
        LSpeed = int((state.LaunchSpeedLeft/255.0)*servo_max)
        RSpeed = int((state.LaunchSpeedRight/255.0)*servo_max)
        print ('LSpeed, Rspeed', LSpeed, RSpeed)
        pwm.set_pwm(pwmA, LSpeed )
        pwm.set_pwm(ain1, 0)
        pwm.set_pwm(ain2, servo_max) 

        time.sleep(1.0)
        pwm.set_pwm(pwmB,  RSpeed )
        pwm.set_pwm(bin1,  0)
        pwm.set_pwm(bin2,  servo_max) 

def launchMotorsOff():

        pwm.set_pwm(pwmA,  0)
        pwm.set_pwm(ain1,  0)
        pwm.set_pwm(ain2,  0) 

        time.sleep(0.5)
        pwm.set_pwm(pwmB,  0) 
        pwm.set_pwm(bin1,  0)
        pwm.set_pwm(bin2,  0) 



def set_servo_pulse(channel, pulse):
    
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, pulse)

def launchServo():
    
    # Move servo on channel O between extremes.
    pwm.set_pwm(0,  state.LaunchServoMin)
    time.sleep(state.LaunchTimeForward)
    pwm.set_pwm(0,  0 )
    time.sleep(state.LaunchTimeDelay)
    pwm.set_pwm(0,  state.LaunchServoMax)
    time.sleep(state.LaunchTimeBackward)
    pwm.set_pwm(0,  0 )
    time.sleep(state.LaunchTimeDelay)
   
def safeShuntdownServos():
    pwm.set_pwm(0,  servo_max)
    time.sleep(state.LaunchTimeQuit)
    pwm = Device(0x41)

def immediateShutDownServos():
    pwm = Device(0x41)


