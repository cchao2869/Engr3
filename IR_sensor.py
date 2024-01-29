# Carolina Chao
# IR Sensor - 1/29/2024

import board
import neopixel
import digitalio

# Basic setup for any sensor:

ir_sensor = digitalio.DigitalInOut(board.D2)        # Set up the IR Sensor using digital pin 2.
ir_sensor.direction = digitalio.Direction.INPUT         # Set the photointerrupter as an input.
ir_sensor.pull = digitalio.Pull.UP           # Use the internal pull-up resistor.

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

c = 0 
last = False

while True:
    if ir_sensor.value == False:        # If object close to sensor (sensor value = LOW)
        print("Obj close.      ", c)
        if last == False:       # Debounce: If state = obj not currently detected
            c = c + 1           # Add to counter
            last = True         # Set state = obj currently detected

    if ir_sensor.value == True:         # If nothing near sensor (sensor value = HIGH) 
        print("No obj detected.", c)
        if last == True:        # Debounce: If state = obj currently detected
            last = False        # Reset state = obj not currently detected

    if(c % 2 != 0):         # If counter is odd number 
        led[0] = (0, 0, 255)        # Neopixel blue
    
    if(c % 2 != 1):             # If counter is even number
        led[0] = (0, 255, 0)       # Neopixel green