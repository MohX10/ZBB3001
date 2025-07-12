# Imports
from machine import Pin
from time import sleep
from ZBB3001 import ZBPD3001, ZBPU3001 # File Import

# Pin Definitions
red = ZBPD3001(0)
green = ZBPU3001(1)

# Main Loop
while True:
  red.main("print('Hello')")
  green.main("print('Goodbye')")
  # These are just examples you can replace the command print() with anything you want
  sleep(0.01)
