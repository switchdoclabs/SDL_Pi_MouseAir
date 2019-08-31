
# provides routine to update MouseAir Blynk Screen
import time
import requests
import json
import state
import traceback
import pixelDriver
import AccessSensors

# Check for user imports
try:
                import conflocal as config
except ImportError:
                import config

import LaunchJob

DEBUGBLYNK = False 
def stopFlash():
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V30?value=0')

def blynkInit():
    # initalize button states
    try:
        if (DEBUGBLYNK):
            print("Entering blynkInit:")


        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V10?value='+str(state.ManualLaunchV10))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V11?value='+str(state.PixelsV11))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V12?value='+str(state.AutoManualSwitchV12))

        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V13?value='+str(state.MotorSpeedV13))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V14?value='+str(state.CatNotCatThresholdV14))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V15?value='+str(state.TriggerSwitchV15))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V16?value='+str(state.EmailPictureV16))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V17?value='+str(state.SetDefaultsV17))
        
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V18?value='+str(state.PixelColorRedV18)+'&value='+ str(state.PixelColorGreenV19)+'&value='+str(state.PixelColorBlueV20))
        print ('rgb=', r.text)


        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V21?value='+str(state.RainbowSpeedV21))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V22?value='+str(state.PixelBrightnessV22))
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V23?value='+str(state.PixelStyleSwitchV23))
        
        
        
        # initialize LEDs
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V29?color=%23FF0000') # red
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V29?value=255') # red
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V30?color=%23FF0000') # red
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V30?value=255') # red
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V31?value='+str(state.UltrasonicTriggerDistanceV31))

        myURL = "http://"+state.LocalIPAddress+":8088/stream.mjpg"
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V33?url="'+myURL+'"') # red
        if (DEBUGBLYNK):
            print("myURL=", myURL)
            print("blynkURL:POST:r.status_code:",r.status_code)

        
        if (DEBUGBLYNK):
            print("Exiting blynkInit:")

    except Exception as e:
        print ("exception in blynkInit")
        print(traceback.format_exc())
        print (e)
        return 0

def blynkResetButton(buttonNumber):
    try:
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/'+buttonNumber+'?value=0')
    except Exception as e:
        print("exception in blynkResetButton")
        print(traceback.format_exc())
        print (e)
        return 0


def blynkStatusTerminalUpdate(entry):
    try:
        put_header={"Content-Type": "application/json"}

        entry = time.strftime("%Y-%m-%d %H:%M:%S")+": "+entry+"\n"
        put_body = json.dumps([entry])
        if (DEBUGBLYNK):
            print("blynkStateUpdate:Pre:put_body:",put_body)
        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V32', data=put_body, headers=put_header)
        if (DEBUGBLYNK):
            print("blynkStateUpdate:POST:r.status_code:",r.status_code)
    except Exception as e:
        print("exception in blynkTerminalUpdate")
        print(traceback.format_exc())
        print (e)
        return 0
    
def blynkSolarTerminalUpdate(entry):
    try:
        put_header={"Content-Type": "application/json"}
        entry = time.strftime("%Y-%m-%d %H:%M:%S")+": "+entry+"\n"

        put_body = json.dumps([entry])
        if (DEBUGBLYNK):
            print("blynkStateUpdate:Pre:put_body:",put_body)
        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V33', data=put_body, headers=put_header)
        if (DEBUGBLYNK):
            print("blynkStateUpdate:POST:r.status_code:",r.status_code)
    except Exception as e:
        print("exception in blynkTerminalUpdate")
        print(traceback.format_exc())
        print (e)
        return 0
    
def blynkUpdateImage():
    #Blynk.setProperty(V1, "urls", "https://image1.jpg", "https://image2.jpg");

    try:
        if (DEBUGBLYNK):
             print("blynkUpdateImage:started")
        """
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?value=2') # Picture URL
        if (DEBUGBLYNK):
             print "blynkUpdateImage:OTHER:r.status_code:",r.status_code
        #r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?urls=http://www.switchdoc.com/2.jpg') # Picture URL
        #r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?urls=http://www.switchdoc.com/skycamera.jpg,http://www.switchdoc.com/2.jpg') # Picture URL
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?value=1;url=http://www.switchdoc.com/skycamera.jpg')
        if (DEBUGBLYNK):
             print "blynkUpdateImage:OTHER:r.status_code:",r.status_code
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?value=2;url=http://www.switchdoc.com/2.jpg') # Picture URL
        if (DEBUGBLYNK):
             print "blynkUpdateImage:OTHER:r.status_code:",r.status_code

        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V70?value=2') # Picture URL
        if (DEBUGBLYNK):
             print "blynkUpdateImage:OTHER:r.status_code:",r.status_code
        """
        
        myURL = "http://"+state.LocalIPAddress+":5000/static/MouseAir"
        
        #r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V40?urls='+myURL+'MouseAirMouseAir.jpg') # Picture URL


        lastPic = int(state.piccount/10)*10
        if (DEBUGBLYNK):
            if (blynkSGSAppOnline() == "true"):
                print("Application Open")
            else:
                if (blynkSGSAppOnline() == "false"):
                    print("Application Closed")
                else:
                    print("Application Bad Value ")

        
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V40?urls='+myURL+str(lastPic)+'.jpg') # Picture URL


    except Exception as e:
        print("exception in blynkUpdateImage")
        print(traceback.format_exc())
        print (e)
        return 0



def blynkStateUpdate():


    try:

        
        blynkUpdateImage()
        
        
        put_header={"Content-Type": "application/json"}

        # set last sample time 
      
        val = time.strftime("%Y-%m-%d %H:%M:%S")  
        put_body = json.dumps([val])
        if (DEBUGBLYNK):
          print("blynkStatusUpdate:",val)
        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V28', data=put_body, headers=put_header)
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POST:r.status_code:",r.status_code)
       
        # do the graphs

        # Ultrasonic Sensor
        val =  AccessSensors.readUltrasonic()
        put_body = json.dumps([val])
        if (DEBUGBLYNK):
          print("blynkStatusUpdate:",val)
        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V24', data=put_body, headers=put_header)
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POST:r.status_code:",r.status_code)

        # CatNotCat Sensor
        val =  AccessSensors.readCatNotCatLevel()
        put_body = json.dumps([val])
        if (DEBUGBLYNK):
          print("blynkStatusUpdate:",val)
        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V25', data=put_body, headers=put_header)
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POST:r.status_code:",r.status_code)

        r = requests.put(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V26', data=put_body, headers=put_header)
        
        # LEDs 


        if (AccessSensors.readMouseDetect()== 1):   
                        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V29?color=%2300FF00') # Green
                        if (DEBUGBLYNK):
                            print("blynkMouseDetect:OTHER:r.status_code:",r.status_code)
        else:
                        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V29?color=%23FF0000') # red


        if (state.CatDetected == True ):   
                        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V30?color=%2300FF00') # Green
                        if (DEBUGBLYNK):
                            print("blynkMouseDetect:LEDCATDETECTED:r.status_code:",r.status_code)
        else:
                        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V30?color=%23FF0000') # red




        return 1
    except Exception as e:
        print("exception in blynkStateUpdate")
        print(traceback.format_exc())
        print (e)
        return 0

def blynkStatusUpdate():

    if (DEBUGBLYNK):
        print("blynkStatusUpdate Entry")
    try:
        put_header={"Content-Type": "application/json"}
        
        # buttons
        #ManualLaunchV10 = 0
        #PixelsV11 = 0
        #AutoManualSwitchV12 = 2

        #MotorSpeedV13 = 240
        #CatNotCatThresholdV14 = 90
        #TriggerSwitchV15 = 4
        #EmailPictureV16 = 0
        #SetDefaultsV17 = 0

        #PixelColorRedV18 = 0
        #PixelColorGreenV19 = 0
        #PixelColorBlueV20  = 200
        #RainbowSpeedV21 = 100
        #PixelBrightnessV22 = 100
        #PixelStyleSwitchV23 = 4



        # look for  manual launch
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V10') # read button state
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBR:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBR:r.text:",r.text)
        
        if (r.text == '["1"]'):
            state.ManualLaunchV10 = True
            blynkStatusTerminalUpdate("Manual Launch of Mouse")
            LaunchJob.launchMouse()
            r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/update/V10?value='+ '0')
            state.ManualLaunchV10 = False

            if (DEBUGBLYNK):
                print("blynkStatusUpdate:POSTBRC:state.ManualLaunchV10 set to True")
        else:
            if(state.ManualLaunchV10 == True):
                blynkStatusTerminalUpdate("Manual launch of Mouse off")
            state.ManualLaunchV10 = False
            if (DEBUGBLYNK):
                print("blynkStatusUpdate:POSTBRC:state.ManualLaunchV10 set to False")

        #PixelsV11 = 0

        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V11') # read button state
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBR:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBR:r.text:",r.text)
       

        if (r.text == '["1"]'):
            state.PixelsV11 = 1 
        else:
            if (state.PixelsV11 == 1):
                pixelDriver.clearPixelStick()
            state.PixelsV11 = 0

        # read pixel style bar
        #PixelStyleSwitchV23 

        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V23') # read button state
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBRV23:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBRV23:r.text:",r.text)
        tempstring = r.text.strip('["')
        state.PixelStyleSwitchV23 = int(tempstring.strip('"]'))
        #print("spixel=", state.PixelStyleSwitchV23)

        
        # read brightness
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V22') # read button state

        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBRV22:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBRV22:r.text:",r.text)
        tempstring = r.text.strip('["')
        tempstring= tempstring.strip('"]')
         
        if (state.PixelBrightnessV22 == int(tempstring)):
                pass
        else:
            state.PixelBrightnessV22 = int(tempstring) 
            pixelDriver.setStripBrightness() 

        # read UltrasonicTriggerDistanceV31
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V31') # read button state

        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBRV22:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBRV22:r.text:",r.text)
        tempstring = r.text.strip('["')
        tempstring= tempstring.strip('"]')
         
        if (state.UltrasonicTriggerDistanceV31 == int(tempstring)):
                pass
        else:
            state.UltrasonicTriggerDistanceV31 = int(tempstring) 
            print("UltraTigger=", state.PixelBrightnessV22)


        #RainbowSpeedV21 = 100
        # read Rainbow Speed
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V21') # read button state

        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBRV21:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBRV21:r.text:",r.text)
        tempstring = r.text.strip('["')
        tempstring= tempstring.strip('"]')
         
        if (state.RainbowSpeedV21 == 100-int(tempstring)):
                pass
        else:
            state.RainbowSpeedV21 = 100-int(tempstring)
            print("rainbowspeed=", state.RainbowSpeedV21)

        #PixelColorRedV18 = 0
        # read color 
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V18') # read button state
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBRV18:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBRV18:r.text:",r.text)
        tempstring = r.text.strip('[')
        tempstring= tempstring.strip(']')
        tempstring= tempstring.replace('"', '')
      
        tempsplit = tempstring.split(",")
        
        
        state.PixelColorRedV18 = int(tempsplit[0])
        state.PixelColorGreenV19 = int(tempsplit[1])
        state.PixelColorBlueV20 = int(tempsplit[2])

        



        '''        
        # turn OLED ON and OFF 
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V6') # read button state
        #if (DEBUGBLYNK):
    
        # look for Flash Strip Command
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/get/V30') # read button state
        if (DEBUGBLYNK):
            print("blynkStatusUpdate:POSTBF:r.status_code:",r.status_code)
            print("blynkStatusUpdate:POSTBF:r.text:",r.text)
   
        
        if (r.text == '["1"]'):
            state.flashStrip = True
            if (DEBUGBLYNK):
                print("blynkStatusUpdate:POSTBRF:state.flashStrip set to True")
        else:
            state.flashStrip = False
            if (DEBUGBLYNK):
                print("blynkStatusUpdate:POSTBRF:state.flashStrip set to False")

         '''


        


        return 1
    except Exception as e:
        print("exception in blynkStatusUpdate")
        print(traceback.format_exc())
        print (e)
        return 0


        
def blynkSGSAppOnline():

    try:
        r = requests.get(config.BLYNK_URL+config.BLYNK_AUTH+'/isAppConnected')
        if (DEBUGBLYNK):
            print("blynkSGSAppOnline:POSTCHECK:r.text:",r.text)
        
        return r.text
    except Exception as e:
        print("exception in blynkApponline")
        print(traceback.format_exc())
        print (e)
        return ""

   
