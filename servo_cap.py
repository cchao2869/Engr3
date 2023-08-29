# Carolina Chao
# Servo Cap Touch
 
import time
import board
import touchio
import pwmio
from adafruit_motor import servo

touch_A1 = touchio.TouchIn(board.A1)  
touch_A2 = touchio.TouchIn(board.A2) 
pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)


while True:
    if touch_A1.value:
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
            print(angle)
    if touch_A2.value:
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
            print(angle)
    time.sleep(0.05)