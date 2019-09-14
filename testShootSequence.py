# MouseAir V3 Launch Sequence

# Check for user imports
try:
    import conflocal as config
except ImportError:
    import config


import Motors
import state
import LaunchJob

LaunchJob.launchMouse()
