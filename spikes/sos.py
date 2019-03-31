'''
Simple python script to signal S O S on an LED.

To setup:
    1. connect the long leg of an LED to a ~50ohm resistor
    2. Connect the other end of the resistor to PIN 23 on the PI
    3. Connect the short leg of the LED to grnd on the PI

To run:
    1. `python sos.py`

To stop:
    1. press ctrl-c
'''

from gpiozero import LED
from time import sleep
led = LED(23)

timeUnit = 0.1
dotTime = 1 * timeUnit
dashTime = 3 * timeUnit
betweenSymbols = 1 * timeUnit
betweenLetters = 3 * timeUnit
betweenWords = 7 * timeUnit

def dot():
    led.on()
    sleep(dotTime)
    led.off()
 
def dash():
    led.on()
    sleep(dashTime)
    led.off()

def morse_s():
    dot()
    sleep(betweenSymbols)
    dot()
    sleep(betweenSymbols)
    dot()

def morse_o():
    dash()
    sleep(betweenSymbols)
    dash()
    sleep(betweenSymbols)
    dash()

while True:
    morse_s()
    sleep(betweenLetters)
    morse_o()
    sleep(betweenLetters)
    morse_s()
    sleep(betweenWords)
