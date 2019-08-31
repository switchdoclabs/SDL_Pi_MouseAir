#!/usr/bin/python3

# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config

import state

import UltraRanger

UltraRanger.getAndPrint()
