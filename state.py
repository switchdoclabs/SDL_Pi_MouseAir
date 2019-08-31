# state file for MouseAir
# replaces Global Variables
#

# tensorflow Keras model
model = None

# MouseAir IP Address
LocalIPAddress = ""

# Launch Motors
LaunchSpeedLeft = 240
LaunchSpeedRight = 240

# Launch Servo

LaunchServoMin = 370
LaunchServoMax = 450

LaunchTimeForward = 1.6
LaunchTimeBackward = 0.8
LaunchTimeDelay = 0.3

LaunchTimeQuit = 0.8

# Button States for Blynk and State

ManualLaunchV10 = 0
PixelsV11 = 1 # Pixel On by default
AutoManualSwitchV12 = 2

MotorSpeedV13 = 240
CatNotCatThresholdV14 = 90
UltrasonicTriggerDistanceV31 = 30
TriggerSwitchV15 = 4
EmailPictureV16 = 0
SetDefaultsV17 = 0

PixelColorRedV18 = 0
PixelColorGreenV19 = 0
PixelColorBlueV20  = 200
RainbowSpeedV21 = 100
PixelBrightnessV22 = 100
PixelStyleSwitchV23 = 4


# Sensor Values

SensorUltrasonicDistance = 0
SensorCatNotCatLevel = 0
SensorMouseDetect = 0

#detection values
CatDetectedNumberOfFrames = 0
CatDetected = False


#blynk count
piccount = 0

# Pixel globals
strip = None


#Locks and Semaphores
PixelLock = None


