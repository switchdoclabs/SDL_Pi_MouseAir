#
#
# object / person detection routines 
# filename: detection.py
# Version 1.0 03/31/14 
#
#


import sys
import time

import utils


sys.path.append('/home/pi/MouseAir/config')
sys.path.append('/home/pi/MouseAir/pclogging')

import pclogging



datalist = [];
# if conflocal.py is not found, import default conf.py

# Check for user imports
try:
	import conflocal as conf
except ImportError:
	import conf


# ultrasonic detect

def initUltrasonic():
	# get range finder working
   	try:
		lastrange = rr.get_range_inch()
		print ("initUltrasonic rangeinch=%f" % rr.get_range_inch())
    	except ValueError:
        	print ("ultrasonic reading error") 

	pclogging.log(pclogging.INFO, __name__, "Ultrasonic Initialized")
	return True

def ultrasonicDetect(distance, repeat ):
	global datalist
	lastrange = 0

   	try:
		lastrange = rr.get_range_inch()
		time.sleep(0.1)
		lastrange = rr.get_range_inch()
		#print("last range = %f" % lastrange)
    	except ValueError:
        	print ("ultrasonic reading error") 
		lastrange = 72
        
	if(lastrange < 1.5):
                lastrange = distance

	if (len(datalist) == 10):
		if (len(datalist) > 0):
			datalist.pop(0)
	datalist.append(lastrange)	
	if (lastrange < distance):
		return True
	else:
		return False


# NFC PY532

def  initNFC():
	
	return True

def NFCDetect():

	return True


# RFID 125KHz ID-3LA

# get RFID from device ID-3LA
# meant to run in a thread and report back to main thread
#
#


def  RFIDrecieveLine(ser):

     timeout = True
     t = 10
                
     st = ''
     initTime = time.time()
     while True:
               st +=  ser.read()
	       if (len(st) > 15):
	       		print("after readline.  st=",st)
			break;
               if timeout and (time.time() - initTime > t) :
                    break


     return st	



def initRFID():

	return True

def RFIDDetect(source, delay, queue):


	time.sleep(delay)

	# setup serial port to ID-3LA

	print("RFID Thread Starting")

	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)



	while True:		
		response = RFIDrecieveLine(ser)
		if (len(response) != 16):
			t =0
			#print("No response=", response)
		else:
			print("Found RFID Card.  response=", response)
			pclogging.log(pclogging.INFO, __name__, "RFID Card Detected:%s" % response)
			queue.put(True)

	
	

	return True


