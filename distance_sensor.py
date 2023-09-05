# Carolina Chao
# Distance Sensor

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)

import board
import digitalio
import pwmio
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
red = pwmio.PWMOut(board.D3)
green = pwmio.PWMOut(board.D5)
blue = pwmio.PWMOut(board.D6)
lcd_columns = 16
lcd_rows = 2
import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)


while True:
    try:
        print((sonar.distance,))
        lcd.message = sonar.distance
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)