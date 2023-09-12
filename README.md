# Circuit Python Intro
## Table of Contents
* [Servo Cap Touch](#ServoCapTouch)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Servo Cap Touch

### Description & Code
Use two touch points (wires) to control a 180 degree servo. 

```python
# Carolina Chao
# Servo Cap Touch
 
import time
import board
import touchio
import pwmio
from adafruit_motor import servo

touch_A1 = touchio.TouchIn(board.A1)    # create capactive touch sensor (wire) from pin A1
touch_A2 = touchio.TouchIn(board.A2)    # create second cap touch sensore from pin A2
pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)    # 
my_servo = servo.Servo(pwm)    # create servo object
angle = 1


while True:
    if touch_A1.value:
            if angle < 174:
                angle = angle + 5    # increase angle by 5 degrees
                my_servo.angle = angle    # update angle to servo
                time.sleep(0.05)
                print(angle)
    if touch_A2.value:
            if angle > 6:
                angle = angle - 5    # decrease angle by 5 degrees
                my_servo.angle = angle    # update angle to servo
                time.sleep(0.05)
                print(angle)
    time.sleep(0.05)
```

### Evidence
![ezgif com-crop](https://github.com/cchao2869/Engr3/assets/91699474/fdee3c52-c49d-4e8b-aea5-b7cd9ed3f63d)

### Wiring
![image](https://github.com/cchao2869/Engr3/assets/91699474/2b579acd-75f0-417e-8ee0-15b4e92ea6d9)

### Reflection
This assignment was really cool, and I'm finally starting to get a hang on Circuit Python. For the past few assignments, the following resources from AdaFruit have been especially helpful to translate from Arduino to Circuit Python:

[Translate](https://learn.adafruit.com/arduino-to-circuitpython?view=all#analog-pwm-output)

[Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)

Through AdaFruit, I found reference code for controlling a 180 degree servo in Circuit Python, as well as a description and code for capacitive touch. It was relatively easy to combine these, so my biggest issue came with the inequalities to control the angle of the servo. Initially, I had the bounds at 180 and 0 degrees. However, I kept running into issues whenever the servo got close to these bounds becausee the loop would stop running since the "angle is out of range". As a solution, I changed the bounds to 174 and 6 degrees since I had the angle variance as +/- 5. This was successful, and the loop runs continuously. I'm very excited to continue to understand Circuit Python, and use capacitive touch in a more complex project in the future.   



## NeoPixel Distance Sensor

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection

[Ultrasonic](https://docs.circuitpython.org/projects/hcsr04/en/latest/api.html)
[NeoPixel](https://learn.adafruit.com/adafruit-metro-m0-express/circuitpython-internal-rgb-led)
[Map_Function](https://www.youtube.com/watch?v=KVLgzVDNV4I)
[elseif](https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch)
