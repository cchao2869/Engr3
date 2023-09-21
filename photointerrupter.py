# Carolina Chao
# Photointerrupter - 9/21/2023

import time
import board
import digitalio

photo = digitalio.DigitalInOut(board.D3)    # photointerrupter connected to digital pin 3
photo.direction = digitalio.Direction.INPUT      # set photointerrupter as a digital input
photo.pull = digitalio.Pull.UP         # set direction of pin pull using internal resistor on Metro board

counter = 0
now = time.monotonic()

while True:
    if photo.value == True:     # if interrupted...
        counter = counter + 1   # add to counter

    if (now + 4) < time.monotonic():  # if 4 seconds elapses
        print("Interupts:", counter)
        now = time.monotonic()       # reset time
        counter = 0     # reset counter
