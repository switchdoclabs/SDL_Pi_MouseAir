#!/usr/bin/python
import time
import RPi.GPIO as GPIO


 
GPIO.setmode(GPIO.BCM)

# RGB LED Module (TEST)
 
#Setup Active states
#Common Anode RGB-LEDs (Active low)
LED_ENABLE = 1
LED_DISABLE = 0
RGB_ENABLE = 0
RGB_DISABLE = 1
 
RGB_RED = 15   
RGB_GREEN = 16 
RGB_BLUE = 18  
RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]
 
def led_setup():
  #Set up the wiring
  GPIO.setmode(GPIO.BOARD)
  # Setup Ports
  for val in RGB:
    GPIO.setup(val, GPIO.OUT)
 
def led_activate(colour):
  GPIO.output(colour,RGB_ENABLE)
 
def led_deactivate(colour):
  GPIO.output(colour,RGB_DISABLE)
 
def led_clear():
  for val in RGB:
    GPIO.output(val, RGB_DISABLE)
 
def main():
  led_setup()
  led_clear()
  led_activate(RGB_RED)
  time.sleep(2)
  led_activate(RGB_GREEN)
  time.sleep(2)
  led_activate(RGB_BLUE)
  time.sleep(2)
  led_deactivate(RGB_RED)
  time.sleep(2)
  led_clear()
  GPIO.cleanup()
 
main()
#End
