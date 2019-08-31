# sensor access functions

# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config

import logging
import state


def readUltrasonic():
    return state.SensorUltrasonicDistance

def readCatNotCatLevel():
    return state.SensorCatNotCatLevel

def readMouseDetect():
    return state.SensorMouseDetect


