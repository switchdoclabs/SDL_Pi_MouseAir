
import time
import RPi.GPIO as GPIO


def measure():
    # This function measures a distance from the Grove Ultrasonic

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.000100)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  stop = start
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  print("time elapsed=", elapsed)
  distance = (elapsed / 0.000147) # in inches at 147uS per inch

  return distance

def measure_average():
  # This function takes 5 measurements and
  # and throws out the highest and lowest
  # returns the average.

  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  time.sleep(0.1)
  distance4=measure()
  time.sleep(0.1)
  distance5=measure()
  time.sleep(0.1)

  distance = distance1 + distance2 + distance3 + distance4 + distance5

  # throw out smallest
  distance = distance - min(distance1, distance2, distance3, distance4, distance5)
  # throw out largest
  distance = distance - max(distance1, distance2, distance3, distance4, distance5)
  distance = distance / 3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 24
GPIO_ECHO    = 23

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)


# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  while True:

    distance = measure_average()
    print ("Distance : %.1f" % distance)
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
