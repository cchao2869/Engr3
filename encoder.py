# Carolina Chao
# Rotary Encoder - 1/2/2024

import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)

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
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    
    menu = ["stop", "caution", "go"]
    menu_index = enc.position
    if last_index == None or menu_index == last_index:    # If your last index is None or your menu index does not match your last index:
        menu_index_lcd = menu_index % 3
        print(menu[menu_index_lcd])    # Print your menu index to the Serial Monitor.
    last_index = menu_index    # Then, set your last index to your menu index.

    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None


