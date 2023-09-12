# Carolina Chao
# Servo Cap Touch - 8/29/2023
 
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