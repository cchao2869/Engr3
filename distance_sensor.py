# Carolina Chao
# Distance Sensor - 9/11/2023


import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)     # create distance sensor object connected to pins D5 and D6

import neopixel
from rainbowio import colorwheel
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
        cm = sonar.distance
        print(cm)
        if cm < 17:                                               # if.. 
            valR = int(map_range(cm, 0, 17, full, 0))
            valB = int(map_range(cm, 0, 17, 0, full))
            valG = 0
            led.fill((valR, valG, valB))
        elif cm < 35:                                             # otherwise, if..
            valB = int(map_range(cm, 17, 35, full, 0))
            valG = int(map_range(cm, 17, 35, 0, full))
            valR = 0
            led.fill((valR, valG, valB))
        else:                                                     # otherwise, do..
            valG = full
            valB = 0
            valR = 0
            led.fill((valR, valG, valB))

    except RuntimeError:                                          # continue running code if issue with ultrasonic sensor distance
        print("Retrying!")
        pass
    time.sleep(0.1)
   