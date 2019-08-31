# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import state
import traceback
from neopixel import *

import AccessSensors

# Check for user imports
try:
            import conflocal as config
except ImportError:
            import config



# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = config.PixelPin      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP


def RGBColor(R,G,B):
        # override color - 
        # Note:  color is G,R,B for some reason
        return  Color(G,R,B)


def setStripBrightness():
    for i in range(0,8):
        state.strip.setBrightness(state.PixelBrightnessV22)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep((wait_ms/1000.0)*state.RainbowSpeedV21/100.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep((wait_ms/1000.0)*state.RainbowSpeedV21/100.0)
		

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
                        for i in range(0, strip.numPixels(), 3):
                            strip.setPixelColor(i+q, wheel((i+j) % 255))
                        strip.show()
                        time.sleep((wait_ms/1000.0)*state.RainbowSpeedV21/100.0)
                        for i in range(0, strip.numPixels(), 3):
                            strip.setPixelColor(i+q, 0)



###############
# Flash LED
###############

def blinkLED(pixel, times, length):

  if (state.PixelsV11 == True):  # only do if Pixels are turned on
    
    state.PixelLock.acquire()

    if (state.PixelStyleSwitchV23 == 4):

        # override color - 
        # Note:  color is G,R,B for some reason
        color = Color(state.PixelColorGreenV19, state.PixelColorRedV18, state.PixelColorBlueV20)
        #if (config.DEBUGMouseAir):
        #    print("N--->Blink LED:%i/%i/%i/%i/%i/%6.2f" % (pixel, state.PixelColorRedV18, state.PixelColorGreenV19, state.PixelColorBlueV20, times, length))

        for x in range(0, times):
            state.strip.setPixelColor(0, color)
            state.strip.show()
            time.sleep(length)
	
        state.strip.setPixelColor(0, Color(0,0,0))
        state.strip.show()

    state.PixelLock.release()


def fill(color):
    for i in range(0,8):
        state.strip.setPixelColor(i,color)

def clearPixelStick():
    state.PixelLock.acquire()

    state.strip.setPixelColor(7,Color(0,0,0))
    state.strip.setPixelColor(6,Color(0,0,0))
    state.strip.setPixelColor(5,Color(0,0,0))
    state.strip.setPixelColor(4,Color(0,0,0))
    state.strip.setPixelColor(3,Color(0,0,0))
    state.strip.setPixelColor(2,Color(0,0,0))
    state.strip.setPixelColor(1,Color(0,0,0))
    state.strip.setPixelColor(0,Color(0,0,0))
    state.strip.show()
    state.PixelLock.release()

def statusLEDs():

  if (state.PixelsV11 == True):  # only do if Pixels are turned on
    state.PixelLock.acquire()
    try:


        if (state.PixelStyleSwitchV23 == 4): # status
            setCatNotCat()

        if (state.PixelStyleSwitchV23 == 3): # rainbow
         while (state.PixelStyleSwitchV23  == 3):
            if (config.DEBUGMouseAir):
                print("3 -rainbow start")
            rainbow(state.strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)
            if (config.DEBUGMouseAir):
                print("rainbow end")
    
         else:
                state.strip.setPixelColor(7,Color(0,0,0))
                state.strip.setPixelColor(6,Color(0,0,0))
                state.strip.setPixelColor(5,Color(0,0,0))
                state.strip.setPixelColor(4,Color(0,0,0))
                state.strip.setPixelColor(3,Color(0,0,0))
                state.strip.setPixelColor(2,Color(0,0,0))
                state.strip.setPixelColor(1,Color(0,0,0))
                state.strip.setPixelColor(0,Color(0,0,0))
                state.strip.show()

        if (state.PixelStyleSwitchV23 == 2): # pulsing
            if (config.DEBUGMouseAir):
                print("2 -pulsing start")

            # slowly power up via blue color
            for i in range(50):
                fill(Color(0, 0, i))
                state.strip.show()
                time.sleep(0.01)

            # blast off!
            fill(Color(255, 0, 0))
            state.strip.show()

            while (state.PixelStyleSwitchV23  == 2):
                # pulse effect
                for i in range(255, 0, -5):
                    fill(Color(i, 0, 0))
                    time.sleep(0.01)
                    state.strip.show()
                for i in range(0, 255, 5):
                    fill(Color(i, 0, 0))
                    time.sleep(0.01)
                    state.strip.show()

            else:
                state.strip.setPixelColor(7,Color(0,0,0))
                state.strip.setPixelColor(6,Color(0,0,0))
                state.strip.setPixelColor(5,Color(0,0,0))
                state.strip.setPixelColor(4,Color(0,0,0))
                state.strip.setPixelColor(3,Color(0,0,0))
                state.strip.setPixelColor(2,Color(0,0,0))
                state.strip.setPixelColor(1,Color(0,0,0))
                state.strip.setPixelColor(0,Color(0,0,0))
                state.strip.show()
 

        if (state.PixelStyleSwitchV23 == 1): # solid
            if (config.DEBUGMouseAir):
                print("1 -solid start")
            # RG swapped for some reason
            color = Color(state.PixelColorGreenV19, state.PixelColorRedV18, state.PixelColorBlueV20)
            state.strip.setPixelColor(7,color)
            state.strip.setPixelColor(6,color)
            state.strip.setPixelColor(5,color)
            state.strip.setPixelColor(4,color)
            state.strip.setPixelColor(3,color)
            state.strip.setPixelColor(2,color)
            state.strip.setPixelColor(1,color)
            state.strip.setPixelColor(0,color)
            state.strip.show()
 
    except:
        print (traceback.format_exc())

    state.PixelLock.release()

def setCatNotCat():

    """ uses 7 top pixels   """
    # 0 - 1/2 of set level- bottom two - RED
    # 1/2 - set level middle  three - YELLOW
    # set equal above set level top = Green

    #We set the top 7 to indicate catnotcat status from AI
    currentCatNotCat = AccessSensors.readCatNotCatLevel()
    color = RGBColor(0,0,0)         
    state.strip.setPixelColor(7,color)
    state.strip.setPixelColor(6,color)
    state.strip.setPixelColor(5,color)
    state.strip.setPixelColor(4,color)
    state.strip.setPixelColor(3,color)
    state.strip.setPixelColor(2,color)
    state.strip.setPixelColor(1,color)
    state.strip.show()

    if (currentCatNotCat >= state.CatNotCatThresholdV14):
       color = RGBColor(0,255,0)         
       state.strip.setPixelColor(7,color)


    pixelCount = int(currentCatNotCat/15)+ 1
    #print("currentCatNotCat =", currentCatNotCat)
    #print("pixelCount =", pixelCount)
    if (pixelCount >= 1):
        color = RGBColor(231, 84, 128)
        state.strip.setPixelColor(1,color)

    if (pixelCount >= 2):
        color = RGBColor(231, 84, 128)
        state.strip.setPixelColor(2,color)

    if (pixelCount >= 3):
        color = RGBColor(231, 84, 128)
        state.strip.setPixelColor(3,color)

    if (pixelCount >= 4):
        color = RGBColor(255, 255, 0)
        state.strip.setPixelColor(4,color)

    if (pixelCount >= 5):
        color = RGBColor(255, 255, 0)
        state.strip.setPixelColor(5,color)

    if (pixelCount >= 6):
        color = RGBColor(255, 255, 0)
        state.strip.setPixelColor(6,color)

       


    state.strip.show()


