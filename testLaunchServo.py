# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import sys

sys.path.append('./PCA9685Driver')
# Import the PCA9685 module.
from pca9685_driver import Device


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Device(0x41)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 370  # Min pulse length out of 4096
servo_max = 450  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel,  pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_frequency(60)

servo_number = 0
print('Moving servo on channel ' + str(servo_number) +' 0, press Ctrl-C to quit...')
try:
    while True:
        # Move servo on channel O between extremes.
        pwm.set_pwm(servo_number,  servo_min)
        time.sleep(1.4)
        pwm.set_pwm(servo_number,  0 )
        time.sleep(0.3)
        pwm.set_pwm(servo_number,  servo_max)
        time.sleep(0.6)
        pwm.set_pwm(servo_number,  0)
        time.sleep(0.3)
except:
    print('shutting down servos')
    pwm.set_pwm(servo_number,  servo_max)
    time.sleep(0.8)
    pwm.set_pwm(servo_number,  0)
    pwm = Device(0x41)
    
