# Carolina Chao
# Stepper Mottor and Limit Switch - 1/10/2024

import board
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01    # variable for time between steps
STEPS = 100     # 100 = 0.5 times full rotation of motor

coils = (       # read 4 coils in motor which control steps (4 wires)
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10), # A2
    digitalio.DigitalInOut(board.D11), # B1
    digitalio.DigitalInOut(board.D12), # B2
)

for coil in coils:          # set digital pins as output
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)   # motor object created

while True:
    for step in range(STEPS):       # 
        motor.onestep(style=stepper.DOUBLE)     # move motor clockwise
        time.sleep(DELAY)

    for step in range(STEPS):
        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)     # move motor counterclockwise and put  motor in  setting for  highest torque for pressing down the limit switch
        time.sleep(DELAY)
