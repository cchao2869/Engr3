# Carolina Chao
# Stepper Mottor and Limit Switch - 1/10/2024

import asyncio
import board
import keypad
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

async def catch_pin_transitions(pin):      # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:           # if limit switch pressed
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):       # 
                        motor.onestep(style=stepper.DOUBLE)     # move motor clockwise
                        time.sleep(DELAY)
                elif event.released:         # if limit switch released
                    print("Limit Switch was released.")
            await asyncio.sleep(0)       # run motor to move to check switch again

async def run_motor():
    while (True):
        for step in range(STEPS):
            motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)     # move motor counterclockwise and put  motor in  setting for  highest torque for pressing down the limit switch
            time.sleep(DELAY)
        await asyncio.sleep(0)       # run limit switch values to move motor again


async def main():
    while (True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))           # run both functions at same time, run motor and check limit switch (call catch_pin_Transitions)
        motor_task = asyncio.create_task(run_motor())          # run both functions at same time, call run_motor to monitor motor value changes
        await asyncio.gather(interrupt_task, motor_task)
asyncio.run(main())



