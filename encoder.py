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


