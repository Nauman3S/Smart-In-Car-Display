
import os
import sys
import signal
import time
import colorsys
import math
try:
    from hyperpixel2r import Touch
    
    display = Hyperpixel2r()
    touch = Touch()

except Exception as e:
    touchH=0



# @touch.on_touch
def handle_touch(touch_id, x, y, state):
    try:
        display.touch(x, y, state)
    except Exception as e:
        touchH=0


try:
    display.run()
except Exception as e:
    touchH=0