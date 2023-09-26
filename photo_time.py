# Carolina Chao
# Photointerrupter Time - 9/26/2023
# Calculate time between interrupts

import time
import board
import digitalio

photo = digitalio.DigitalInOut(board.D3)    # photointerrupter connected to digital pin 3
photo.direction = digitalio.Direction.INPUT      # set photointerrupter as a digital input
photo.pull = digitalio.Pull.UP         # set direction of pin pull using internal resistor on Metro board

state = 0    # last interrupt state
counter = 0     # number of interrupts
last = 0
t = 0
mark = 0


while True:

    if photo.value == False and counter > 0:    # if not currently interrupted and has been interrupted
        state = 0       # reset interrupt state to not previously interrupted

    if state == 0:      # if previously uninterrupted
        if photo.value == True:     # if currently interrupted...
            t = int(time.monotonic() - last)
            print(t, "seconds")
            last = time.monotonic()
            counter = counter + 1   # add to counter
            state = 1       # set state to previously interrupted
            







