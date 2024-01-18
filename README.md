
# Engineering 3 
* [Circuit Python Intro](#CircuitPythonIntro)
* [Onshape Certification Prep](#OnshapeCertificationPrep)
* [Circuit Python Intermediate](#CircuitPythonIntermediate)
---
---
---
# Circuit Python Intro
## Table of Contents
* [Servo Cap Touch](#ServoCapTouch)
* [Neopixel Distance Sensor](#NeopixelDistanceSensor)
* [Motor Control](#MotorControl)
* [Photointerrupter](#Photointerrupter)
* [Interrupt Time Interval](#InterrruptTimeInterval)
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
This assignment was really cool, and I'm finally starting to get a hang on Circuit Python. For the past few assignments, the following resources from AdaFruit have been especially helpful to translate from Arduino to Circuit Python (shown below).

Through AdaFruit, I found reference code for controlling a 180 degree servo in Circuit Python, as well as a description and code for capacitive touch. It was relatively easy to combine these, so my biggest issue came with the inequalities to control the angle of the servo. Initially, I had the bounds at 180 and 0 degrees. However, I kept running into issues whenever the servo got close to these bounds becausee the loop would stop running since the "angle is out of range". As a solution, I changed the bounds to 174 and 6 degrees since I had the angle variance as +/- 5. This was successful, and the loop runs continuously. I'm very excited to continue to understand Circuit Python, and use capacitive touch in a more complex project in the future.   

### Resources
[Translate Arduino to Circuit Python](https://learn.adafruit.com/arduino-to-circuitpython?view=all#analog-pwm-output)

[Circuit Python Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)


## NeoPixel Distance Sensor

### Description & Code
Use an ultrasonic sensor to measure distance to an object, and fade color of neopixel based on distance. 


```python
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
        if cm < 18:                                               # if.. 
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
```

### Evidence
![ezgif-4-fba71c1030](https://github.com/cchao2869/Engr3/assets/91699474/e8303cc0-1790-4d27-a6ad-4e70ad1d4969)

### Wiring
![image](https://github.com/cchao2869/Engr3/assets/91699474/8d5f7ec7-05d2-4e76-98bf-f0d55e6c79ad)

### Reflection
The most difficult part of this assignment was getting the neopixel to work and map smoothly. To get the neopixel to fade smoother, I used a math function to turn the float sonar.distance from the ultrasonic sensor library to an integer. Example code for the ultrasonic sensor was relatively easy to find and get working, but neopixel was much more difficult. Another issue throughout this assignment was that the Metro Express kept crashing after I tried to upload code. To fix this, I replaced my adafruit library with an older version. 

### Resources
[Ultrasonic Sensor](https://docs.circuitpython.org/projects/hcsr04/en/latest/api.html)

[NeoPixel](https://learn.adafruit.com/adafruit-metro-m0-express/circuitpython-internal-rgb-led)

[Map_Function](https://www.youtube.com/watch?v=KVLgzVDNV4I)

[elseif](https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch)


## Motor Control

### Description & Code
Use a potentiometer to control a DC motor. 

```python
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
```

### Evidence
![ezgif-5-c88c139284](https://github.com/cchao2869/Engr3/assets/91699474/7a7bc879-b973-4d9d-afbf-cca9230e285b)

### Wiring
![IRLB8721 Motor Control](https://github.com/cchao2869/Engr3/assets/91699474/c49197e4-4e49-4573-85a1-0e6f627b0c98)
 
![image](https://github.com/cchao2869/Engr3/assets/91699474/dc3c54a9-4515-4b2e-892e-fac8d5fc2f76)

### Reflection
The code for this assignment was very simple. Initially, I thought a map function was necessary to control the motor speed based on the potentiometer value. However, duty cycle is more efficient, and once I understood what duty cycle is, the assignment was easy. Duty cycle is a non-negative number that represents the percent of time that a part of the PWM signal is fully on vs. fully off. Duty cycle can be thought of as a percentage, where at 0% the signal is always turned off and never turns on, at 50% the signal is on for exactly as much time as it’s off, and at 100% it’s always turned on. Therefore, the duty cycle of the motor can be set equal to the potentiometer value (between 0 and 65535), and the motor speed will map accordingly. As a reminder, digital inputs and outputs can only be ON or OFF, whereas analog inputs and outputs have variance.

### Resources
[Potentiometer](https://learn.adafruit.com/make-it-change-potentiometers/circuitpython)
[Duty Cycle and PWM](https://learn.adafruit.com/circuitpython-basics-analog-inputs-and-outputs/pulse-width-modulation-outputs)


## Photointerrupter

### Description & Code
Use a photointerrupter to count how many times it has been interrupted in a four second interval. 

```python
# Carolina Chao
# Photointerrupter - 9/21/2023

import time
import board
import digitalio

photo = digitalio.DigitalInOut(board.D3)    # photointerrupter connected to digital pin 3
photo.direction = digitalio.Direction.INPUT      # set photointerrupter as a digital input
photo.pull = digitalio.Pull.UP         # set direction of pin pull using internal resistor on Metro board

state = 0 
counter = 0     # number of interrupts
now = time.monotonic()

while True:

    if photo.value == False:    # if not currently interrupted
        state = 0       # reset interrupt state to not previously interrupted

    if state == 0:      # if previously uninterrupted
        if photo.value == True:     # if currently interrupted...
            counter = counter + 1   # add to counter
            state = 1       # set state to previously interrupted


    if (now + 4) < time.monotonic():  # if 4 seconds elapses
        print("Interupts:", counter)
        now = time.monotonic()       # reset time
        counter = 0     # reset counter
```

### Evidence
![ezgif-5-adce547abb](https://github.com/cchao2869/Engr3/assets/91699474/0f13d342-fe36-485b-a5c4-d14c11716858)
![image](https://github.com/cchao2869/Engr3/assets/91699474/c1dc48e2-4f14-4e54-ac63-a1c9a52ed157)

### Wiring
![Final photointerrupter fritzing diagram image1](https://github.com/cchao2869/Engr3/assets/91699474/b3c997a9-5f50-4c79-a158-d7bdc45d98c8)

### Reflection
I enjoyed this assignment, as it helped me solidify how to set up a digital pin with Circuit Python, and I learned how to debounce a photointerrupter with nested ```if``` statements. Additionally, I learned a new way to count using ```time.monotonic``` instead of just a delay using ```time.sleep```. It was fairly easy to get the photointerrupter running and counting the number of interrupts, but it took me a few tries to correctly use ```if``` statements to debounce the photointerrupter. I solved this issue by making another varible for the previous interrupt state (```state```), instead of just the ```photo.value```, which shows the current state of the photointerrupter. 

### Evidence 
![ezgif-5-adce547abb](https://github.com/cchao2869/Engr3/assets/91699474/0f13d342-fe36-485b-a5c4-d14c11716858)

### Resources
[```time.monotonic```](https://learn.adafruit.com/arduino-to-circuitpython/time)

[```digitalio```](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/#digitalio.DigitalInOut)


## Interrupt Time Interval

### Description & Code
Use a photointerrupter to count time between interrupts. 

```python
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
            
```

### Wiring
![Final photointerrupter fritzing diagram image1](https://github.com/cchao2869/Engr3/assets/91699474/b3c997a9-5f50-4c79-a158-d7bdc45d98c8)

### Reflection
The hardest part of this assignment was understanding what time intervals to count and how to use ```time.monotonic()```. ```time.monotonic``` counts the time in seconds from when the board gets power. In order to count the time interval between interrupts, I had to manipulate ```time.monotonic``` with the variables ```last``` and ```t```. ```last``` represents the time beginning at the first interrupt, and ```t``` is the current time (```time.monotonic```) subracted from the time at the first interrupt. The order to each line was important for this assignment. By writing the line defining ```t```, and printing that before ```last```, the time since the last interrupt is correctly printed. 

---
---
# Onshape Certification Prep
## Table of Contents
* [Block Hanger](#BlockHanger)
* [Swing Arm](#SwingArm)
* [Single Part](#SinglePart)
* [CAD Challenge - Wheel](#CADChallenge-Wheel)
* [Multi-Part Cylinder](#Multi-PartCylinder)
* [Microphone Stand](#MicrophoneStand)
---

## Block Hanger

### Description

Use a drawing to design a simple block hanger. 

### Evidence
![image](https://github.com/cchao2869/Engr3/assets/91699474/70692a77-fc97-471a-9d3a-a68c3d25ffa8) 
Isometric view. 
![image](https://github.com/cchao2869/Engr3/assets/91699474/476b37d1-28ec-4cf8-8b7e-c1e3605c1045)
Front view. 
![image](https://github.com/cchao2869/Engr3/assets/91699474/45afb6ec-0884-49e8-b91c-1f1c70b54e11)
Top view. 


### Part Link 

[Block Hanger](https://cvilleschools.onshape.com/documents/dc5e3e08fa60365adaf235d4/w/b8a016bdc84f26997116b1ff/e/fbf688942fb4a090461fd879?renderMode=0&uiState=651c3c5634ee5a40dcda60f2)

### Reflection
This assignment was a good transition to Onshape, but fairly easy as it only took one main sketch, and then a few extrudes to remove holes. In order to design this part efficiently, I used the Symmetric tool. In addition, when using the Extrude tool to remove from the part, it is important to set the End Type to Through All (unless another is desired). This will prevent unwanted removal of areas in large, complicated Part Studios. Remember to completly constrain a sketch (no blue, all black) before extruding!

## Swing Arm

### Description

Use drawings to design a swing arm with variables that can be adjusted to practice for the Onshape Certification Exam. 

### Evidence

![image](https://github.com/cchao2869/Engr3/assets/91699474/6e267858-93bc-468d-b62a-6cb0fedadde0) 
Isometric view configuration 1.
![image](https://github.com/cchao2869/Engr3/assets/91699474/18d5c5e2-0949-44d1-a186-970be5f85ab4) 
Isometric view configuration 2. 
![image](https://github.com/cchao2869/Engr3/assets/91699474/62866caf-85ab-49ff-bac1-b07f703fa9e1)
Side view configuration 1.
![image](https://github.com/cchao2869/Engr3/assets/91699474/6f4065fb-f8d4-425e-99d4-dcaf9ce3328f)
Front view configuration 1. 

### Part Link 

[Swing Arm](https://cvilleschools.onshape.com/documents/3a08f93e624b27da27233aaa/w/58e2e113dcc8ff706ccf9cab/e/004696c950245ba8d0a95735?renderMode=0&uiState=651c2dd3ee66814d9a8f4d13)

### Reflection

This was good practice at using drawings to create a part on Onshape, as well as variables which are used in the Certification Exam I will take in the spring. Although there is not a "right" way to create a part, there are certainly ways to make a part that are less efficient, and lead to errors later on when dimensions need to be changed (such as with varibles). For instance, Mr. Dierof advised me to never use fillets as opposed to sketch fillets. I also thought it was interesting that Mr. Miller said he creates parts by beginning with a solid block and removing necessary pieces (mirroring the way a machine would manufacter the part). As a reminder, TYP means typical (referring to measurements). If a measurement has TYP next to it, it means similar entities have the same measurement. I ran into a few issues when reading the drawings. It is important to differentiate between the symbol for radius as opposed to diameter. For example, a circle of diameter 10 could be dimensioned as R5 or ⌀10. Additionally, the distance between the center of a circle and the edge is not the diameter, but half the length of the width (shown below). Finally, I learned how to read sectioned drawings. The dashed line shows exactly where the section is with the arrow pointing towards the direction of the face, and all shaded areas are solid. 

## Single Part

### Description

Use drawings to design a single part with variables that can be adjusted for a series of questions.  

### Evidence

![image](https://github.com/cchao2869/Engr3/assets/91699474/19b87c9d-59ab-4dae-a309-df7c70de8c60)
Front view configuration 1. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/8abc8fe7-b50b-47ed-9dcb-5f6f1e025cdb)
Side view configuration 2.

![image](https://github.com/cchao2869/Engr3/assets/91699474/5a4c1a62-17f7-4bbd-a01f-3b1422ab14c0)
Isometric view configuration 5. 


### Part Link 

[Single Part](https://cvilleschools.onshape.com/documents/c614b06d788cb2a3258e93e6/w/5742773ecaed99d6753b411e/e/924ea11a6697a511774fdc18?renderMode=0&uiState=654127416559cc4a6485e145)

### Reflection

This was a fairly easy part to design, as it is symmetrical, but it was still good practice of fundamentals for the Onshape Exam. For instance, although my first instinct was to use a Sketch Mirror to speed up the process of designing this part, Mr. Miller explained to me that a Part Mirror is better because it causes less issues later on (Sketch Mirrors can easily break). So, I sketched one half of the part, and then mirrored it after I extruded it. I also used a Feature Mirror to create the removed section (with an extrude) on both sides of the part. One issue I ran into is that I thought the two holes on top of the part could be created with the Hole Counterbore feature. However, because the depth of the inital removed section was dimentioned, these holes should be made with removed circles and a chamfer. After I finished the first configuration, I had an easy time with the next five because I made several variables and versions for each question. It is helpful to look ahead at all the questions, and create variables for dimensions that change (or at least those that change several times). Creating versions for each question was helpful if I needed to go back and forth between configurations. 


## CAD Challenge - Wheel

### Description
Design a wheel based off drawings as quick as possible with the fewest number of features. 

### Evidence
![image](https://github.com/cchao2869/Engr3/assets/91699474/6d47db93-85d3-47fe-9989-a3d861429872)

Isometric view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/619328a7-ec3d-4bff-b825-24886ebb979d)

Top view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/7321b6fd-31fd-4115-b477-acc86aa1cb1e)

Front view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/b75d763d-e09d-4f6a-8e78-cda66c2c1ce3)

Performance model. 

### Part Link 

[Wheel](https://cvilleschools.onshape.com/documents/0456890d7aa8f67fc5270900/w/00f0803b3dc99da3b8cd2f42/e/7fbbfec565f818dcf56dadc6?renderMode=0&uiState=6543c281a607f210024531c8)

### Reflection

This part was difficult, and I initially approached it the wrong way. I started by making a sketch of the top face, but I realized it was much easier to sketch the side section view, and revolve it. For drawings which include a section view in the middle of a circular symmetric part, it is often easier to revolve the section view (be aware - only extrude solid areas, those that are shaded). Another issue I had with this part was constraining the removed arc areas. Although it was not specifically dimentioned in the drawing, the edges of the removed areas pass through the origin as shown below. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/c0e5e142-edd4-49c5-974b-c39672b23927)


## Multi-Part Cylinder

### Description
Use drawings to create a multi-part cylinder with variables for different configurations. 

### Evidence

![image](https://github.com/cchao2869/Engr3/assets/91699474/b1417324-af12-46c7-ae60-0c73c8fb8222)

Isometric view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/8b1f2f1a-2325-4ff3-b738-eb3da029b061)

Side view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/e8326b0c-424c-4467-89c9-e9f0ec8f1546)

Side section view. 

### Part Link 
[Multi-Part Cylinder](https://cvilleschools.onshape.com/documents/fc9491b76efd0795a2eb9a68/w/af227b52b9a197610ab03729/e/e79f10972489fbd2a8f1f00a?renderMode=0&uiState=654bb2b556ae3f1431d828a9)

### Reflection

This assignment was fun and used a variety of skills. As always, I began by looking over the configurations and creating variables for dimentions that will change in future questions. This helped greatly speed up the time to edit my multi-part after I made the first configuration. It is important to note that the part should not be created off all dimentions listed. Dimentions in parethesis as shown below are only for reference, as they will change in future configurations. It is helpful to go back and forth from the design intent and individual part drawings, because the design intent often has the actual dimentions the part should be based off of. With design intents, it can be helpful to use a extrude with a second end position. One feature that confus3ed me was the inner edge of the top cap. Although this initially appears like a chamfer or fillet, the way to create this inverse fillet is to sketch the radius as a section view, and revolve remove the arc (see below). Finally, be aware of where parts are solid or hollow with shaded regions. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/50f0d860-2416-45cf-b74d-6ee4c643ffc8)

![image](https://github.com/cchao2869/Engr3/assets/91699474/3f2c3a02-35b9-462a-ba51-74a5555f41d8)

Desgin intent and paranthetial dimentions. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/e2cd3fec-8d82-4616-b137-dc2f9f72d88c)

![image](https://github.com/cchao2869/Engr3/assets/91699474/3bc19064-684d-4fa1-9244-c2d9f3787817)

Reverse fillet revolve. 

## Microphone Stand Assembly

### Description
Use drawings and variables to create a microphone stand and assmeble it using a screw. 
### Evidence

![image](https://github.com/cchao2869/Engr3/assets/91699474/d4ac55e0-7667-4fe3-86be-b17f73949968)

Isometric view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/a72c9709-6d71-414a-945f-27619a2c33d1)

Front view. 

![image](https://github.com/cchao2869/Engr3/assets/91699474/bb90c024-9a30-43c3-a73a-78a59cc5d214)

Front section view. 

### Part Link 

[Microphone Stand Assembly](https://cvilleschools.onshape.com/documents/02d00aa08437ba3201fccadc/w/65c4c3db295472020c20516c/e/2d579a46d523769475dd7de6?renderMode=0&uiState=654bba3ef1cfc3529c883f48)

### Reflection
This assignment was fairly easy, but a good refresher in assemblies. With this part, I created variables for almost every dimention that changed with the different configurations, except the ones that only changed once in the final configuration. To make sure the part worked correctly when dimentions were changed, I based dimentions off the design intent as opposed to individual part so that the parts changed together. I also used revolves as much as possible when given circular section views. One feature that confused me was the inner filler on the Mic Holder. The outer edge is dimentioned to have a 10mm radius, with the outer and inner edge always 3mm apart. Making the inner fillet also a radius of 10 did not maintain the 3mm distance. Instead, the inner fillet was 7mm because of the circles and distance between them (see below). Be aware of material changes with different configurations as well. 


![image](https://github.com/cchao2869/Engr3/assets/91699474/2c66c86d-757c-45c2-9da0-ebccee51e0a2)

Mic Holder fillets. 

---
---

# Circuit Python Prep

## Table of Contents
* [Rotary Encoder Traffic Light](#RotaryEncoderTrafficLight)
* [Stepper Motor and Limit Switch](#StepperMotorandLimitSwitch)
---

## Rotary Encoder Traffic Light

### Description & Code
Use a rotary encoder to change the color of the neopixel from an array of options displayed on the LCD screen. 

```python
# Carolina Chao
# Rotary Encoder - 1/2/2024

import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)  # create lcd obj

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)  # enc = rotaryio.IncrementalEncoder(CLK pin, DT pin, increments)
last_index = None
menu_index = 0

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None


while True:

    menu = ["stop", "caution", "go"] # create array
    menu_index = enc.position  # array connected to encoder position
    if last_index == None or menu_index == last_index:    # If your last index is None (encoder has not been used) or your menu index does not match your last index (has been moved):
        menu_index_lcd = menu_index % 3 
        print(menu[menu_index_lcd])    # Print your menu index to the Serial Monitor.
    last_index = menu_index    # Then, set your last index to your menu index - update.

    if not button.value and button_state is None:  # debounce: if button was pressed, not currently
        button_state = "pressed" # button can be pressed
    if button.value and button_state == "pressed":  # if button can be pressed and is currently pressed
        print("Button is pressed")
        button_state = None # reset, button was pressed

    lcd.set_cursor_pos(0,0) # (row, column) - upper left position
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0) # second row
    lcd.print("          ")  # erase previous characters
    lcd.set_cursor_pos(1,0)  # set cursor back to beginning of second row
    lcd.print(menu[menu_index_lcd])  # print array

    if menu_index_lcd == 0 and button_state == "pressed":  # if on "stop" and button currently pressed
        led[0] = (255, 0, 0)  # set neopixel to red
    if menu_index_lcd == 1 and button_state == "pressed":
        led[0] = (255, 255, 0)
    if menu_index_lcd == 2 and button_state == "pressed":
        led[0] = (0, 255, 0)

```

### Evidence
![ezgif-4-8dd76563de](https://github.com/cchao2869/Engr3/assets/91699474/730ac988-450a-4c73-8370-6c2e1e63c54e)

### Wiring
![image](https://github.com/cchao2869/Engr3/assets/91699474/f251728c-51d7-47d8-97dc-7d5e0868b7f8)

### Reflection
Although the coding for this assignment was simple, I ran into several problems using VS Code and uploading the LCD libraries. Some of these include powering the LCD and board at the same time (must unplug LCD power first) and inability to access the library folder (delete and redownload). As for the code, it was simple when broken up into different steps. First, I got the rotary encoder working as a button. With a quick few lines to debounce the button (using both button_state and button.value), this was accomplished. Next, I worked on cycling through the menu with a three option array. I used modulo % 3 to make sure every encoder position returns menu[0], menu[1], or menu[2]. Finally, I set up the LCD to display the menu, and used simple ```if``` statements to control the neopixel. This assignment taught me the value in dividing a difficult problem into managable steps, in order to complete the task with ease and precision, as it is easier to identify where a problem lies if one arises. 

## Stepper Motor and Limit Switch

### Description & Code
Use a limit switch to control the range of a stepper motor. 

```python
# Carolina Chao
# Rotary Encoder - 1/2/2024

import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)  # create lcd obj

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)  # enc = rotaryio.IncrementalEncoder(CLK pin, DT pin, increments)
last_index = None
menu_index = 0

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None


while True:

    menu = ["stop", "caution", "go"] # create array
    menu_index = enc.position  # array connected to encoder position
    if last_index == None or menu_index == last_index:    # If your last index is None (encoder has not been used) or your menu index does not match your last index (has been moved):
        menu_index_lcd = menu_index % 3 
        print(menu[menu_index_lcd])    # Print your menu index to the Serial Monitor.
    last_index = menu_index    # Then, set your last index to your menu index - update.

    if not button.value and button_state is None:  # debounce: if button was pressed, not currently
        button_state = "pressed" # button can be pressed
    if button.value and button_state == "pressed":  # if button can be pressed and is currently pressed
        print("Button is pressed")
        button_state = None # reset, button was pressed

    lcd.set_cursor_pos(0,0) # (row, column) - upper left position
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0) # second row
    lcd.print("          ")  # erase previous characters
    lcd.set_cursor_pos(1,0)  # set cursor back to beginning of second row
    lcd.print(menu[menu_index_lcd])  # print array

    if menu_index_lcd == 0 and button_state == "pressed":  # if on "stop" and button currently pressed
        led[0] = (255, 0, 0)  # set neopixel to red
    if menu_index_lcd == 1 and button_state == "pressed":
        led[0] = (255, 255, 0)
    if menu_index_lcd == 2 and button_state == "pressed":
        led[0] = (0, 255, 0)

```

### Evidence
![ezgif-4-8dd76563de](https://github.com/cchao2869/Engr3/assets/91699474/730ac988-450a-4c73-8370-6c2e1e63c54e)

### Wiring

### Reflection
Although the coding for this assignment was simple, I ran into several problems using VS Code and uploading the LCD libraries. Some of these include powering the LCD and board at the same time (must unplug LCD power first) and inability to access the library folder (delete and redownload). As for the code, it was simple when broken up into different steps. First, I got the rotary encoder working as a button. With a quick few lines to debounce the button (using both button_state and button.value), this was accomplished. Next, I worked on cycling through the menu with a three option array. I used modulo % 3 to make sure every encoder position returns menu[0], menu[1], or menu[2]. Finally, I set up the LCD to display the menu, and used simple ```if``` statements to control the neopixel. This assignment taught me the value in dividing a difficult problem into managable steps, in order to complete the task with ease and precision, as it is easier to identify where a problem lies if one arises. 




