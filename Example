# Imports
from machine import Pin
from time import sleep
from ZBB3001 import ZBPD3001, ZBPU3001 # File Import

# Pin Definitions
red = ZBPD3001(0)
green = ZBPU3001(1)

# Main Loop
while True:
  red.main("print('Sucessful Interrupt on Pin 0')")
  green.main("print('Sucessful Interrupt on Pin 1')")
  sleep(0.01)
