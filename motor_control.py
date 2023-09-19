# Carolina Chao
# Motor Control - 9/18/2023

import time
import board
from analogio import AnalogIn
import pwmio

potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1
motor = pwmio.PWMOut(board.D3)  # motor connected to D3


while True:

    print((potentiometer.value))      # Display value
    motor.duty_cycle = potentiometer.value  # motor power modulation based on potentiometer value
    time.sleep(0.25)                   # Wait a bit before checking all again