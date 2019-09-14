# launch Thread

# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config

import logging

import traceback
import state
import time
import updateBlynk

import Motors 

def launchMouse():

        time.sleep(1.0)




        # Step 1 - Start Motors

        print("Step 1 - Motors Starting")
    
        Motors.launchMotorsOn()


        # Step 2 - Launch Mouse 
        print("Step 2 - Mouse Launch Servo Starting")
        Motors.launchServoStart()    

        # Step 3 - Stop Motors
        print("Step 3 - Motors Stopping")
        Motors.launchMotorsOff()

        # Step 4 - Launch Mouse 
        print("Step 4 - Mouse Launch Servo Starting")
        Motors.launchServoRetract()    


        print("Step 5- Ready for Next Launch")    


def checkForLaunch():

  if (state.AutoManualSwitchV12 == 1): # auto launch
    if (state.CatDetected == True):

        if (state.SensorMouseDetect == 1):
            print("##############")
            print("Launch Mouse")
            print("##############")
        
            launchMouse()
            if (config.USEBLYNK):
                updateBlynk.blynkStatusTerminalUpdate("Mouse Launched" ) 
            state.CatDetected = False
            state.CatDetecteNumberOfFrames = 0
        else:
            print("##############")
            print("Mo Mouse Detected ")
            print("Launch Canceled")
            print("##############")
            if (config.USEBLYNK):
                updateBlynk.blynkStatusTerminalUpdate("Launch Cancelled -NMD" ) 

            state.CatDetected = False
            state.CatDetecteNumberOfFrames = 0

    else:
       if(state.ManualLaunchV10 == 1): # launch the mouse
         launchMouse()
         if (config.USEBLYNK):
             updateBlynk.blynkStatusTerminalUpdate("Manual Mouse Launched" ) 
         state.CatDetected = False
         state.CatDetecteNumberOfFrames = 0

  else: # since manual is detected, turn off CatDetected
      state.CatDetected = False
      state.CatDetecteNumberOfFrames = 0

