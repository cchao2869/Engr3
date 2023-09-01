# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Servo Cap Touch](#Servo Cap Touch)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Servo Cap Touch

### Description & Code
Use two touch points (wires) to control a 180 degree servo. 

```python


```


### Evidence


Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
This assignment was really cool, and I'm finally starting to get a hang on Circuit Python. For the past few assignments, the following resources from AdaFruit have been especially helpful to translate from Arduino to Circuit Python:

[Translate](https://learn.adafruit.com/arduino-to-circuitpython?view=all#analog-pwm-output)

[Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)

Through AdaFruit, I found reference code for controlling a 180 degree servo in Circuit Python, as well as a description and code for capacitive touch. It was relatively easy to combine these, so my biggest issue came with the inequalities to control the angle of the servo. Initially, I had the bounds at 180 and 0 degrees. However, I kept running into issues whenever the servo got close to these bounds becausee the loop would stop running since the "angle is out of range". As a solution, I changed the bounds to 174 and 6 degrees since I had the angle variance as +/- 5. This was successful, and the loop runs continuously. I'm very excited to continue to understand Circuit Python, and use capacitive touch in a more complex project in the future.   



## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
