"""
I made this code to make adding interrupts for pushbuttons easier

Here is my github account link
https://github.com/MohX10

"""


# Imports
from machine import Pin
from time import ticks_ms, sleep_ms


# Variables and Interrupt for pull down button
stamp = 1
pressed_time = None
button_pressed = False


def cb1(pin):
    global button_pressed, pressed_time, stamp
    pressed_time = ticks_ms()
    if pressed_time - stamp >= 200:
        button_pressed = True
        stamp = pressed_time


# Variables and Interrupt for pull up button
stamp1 = 2
pressed_time1 = None
button_pressed1 = True
def cb2(pin):
    global button_pressed1, stamp1, pressed_time1
    pressed_time1 = ticks_ms()
    if pressed_time1 - stamp1 >= 200:
        button_pressed1 = False
        stamp1 = pressed_time1


# Definition of a button with a pull down resistor
class ZBPD3001:
    def __init__(self, num):
        self.num = num
        self.pin = Pin(num, Pin.IN, Pin.PULL_DOWN)
        # Pin Declaration

        self.pin.irq(trigger=Pin.IRQ_RISING, handler=cb1)
        # IRQ Interrupt Handler


    def value(self):
        return self.pin.value()
        # This returns the value of the pin (Default=0)


    # Main Function (This will be put in your code)
    def main(self, sth):
        global button_pressed
        if button_pressed:
            if self.pin.value():
                exec(sth)
                sleep_ms(50) # Tiny Delay to avoid bouncing
            button_pressed = False

        # Double Check to ensure that everything executes properly
        # Executing a command implemented by user in exec()
        # Reseting the Identifier

# Definition of a button with a pull up resistor
class ZBPU3001:
    def __init__(self, num):
        self.num = num
        self.pin = Pin(num, Pin.IN, Pin.PULL_UP)
        # Pin Declaration

        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=cb2)


    def value(self):
        return self.pin.value()
        # This returns the value of the pin (Default=1)


    def main(self, sth):
        global button_pressed1
        # Main Function (This will be put in your code)


        if not button_pressed1:
            if not self.pin.value():
                exec(sth)
                sleep_ms(50) # Tiny Delay to avoid bouncing
            button_pressed1 = True
            # Double Check to ensure that everything executes properly
            # Executing a command implemented by user in exec()
            # Reseting the Identifier
