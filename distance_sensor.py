# Carolina Chao
# Distance Sensor - 9/11/2023


import math
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)     # create distance sensor object connected to pins D5 and D6

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)                        # create 1 led object on metro board
led.brightness = (0.3)                                            # set led brightness to 30%
valR = 0
valG = 0
valB = 0
cm = 0
from adafruit_simplemath import map_range
full = 65535


while True:
    try:
        cm = math.ceil(sonar.distance)                            # round sonar.distance to integer and call as "cm"
        print(cm)
        led.fill((valR, valG, valB))
        if cm < 6:                                                # if..
            valR = full
            valG = 0
            valB = 0
        elif cm < 25: 
            valR = int(map_range(cm, 0, 25, full, 0))
            valB = int(map_range(cm, 0, 25, 0, full))
            valG = 0
        elif cm < 35:                                             # otherwise, if..
            valB = int(map_range(cm, 25, 35, full, 0))
            valG = int(map_range(cm, 25, 35, 0, full))
            valR = 0
        else:                                                     # otherwise, do..
            valG = full
            valB = 0
            valR = 0

    except RuntimeError:                                          # continue running code if issue with ultrasonic sensor distance
        print("Retrying!")
        pass
    time.sleep(0.1)
   