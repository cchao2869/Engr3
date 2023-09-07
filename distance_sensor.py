# Carolina Chao
# Distance Sensor


import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

from rainbowio import colorwheel
import neopixel

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = (0.3)


while True:
    print((sonar.distance,))
    time.sleep(0.1)

    if sonar.distance < 34:
        led[0] = (255, 0, 0)
    
    if sonar.distance > 34:
        led[0] = (0, 255, 0)