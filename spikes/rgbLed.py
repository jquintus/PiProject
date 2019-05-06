'''
Simple python script to play with an RGB LED
https://gpiozero.readthedocs.io/en/stable/recipes.html#full-color-led
(I didn't get this working because my LEDs were not the same type as expected in the example)

To setup:

To run:
    1. `python rgbLed.py`
'''

from gpiozero import RGBLED
from time import sleep


led = RGBLED(red=9, green=10, blue=11)

print ("full red")
led.red = 1
sleep(1)

print("Half red")
led.red = 0.5
sleep(1)


print("full green")
led.color = (0, 1, 0)
sleep(1)

print("magenta")
led.color = (1, 0, 1)
sleep(1)

print("yellow")
led.color = (1, 1, 0)
sleep(1)

print("cyan")
led.color = (0, 1, 1)
sleep(1)

print("white")
led.color = (1, 1, 1)
sleep(1)

print("off")
led.color = (0, 0, 0)
sleep(1)

print("slowly increase intensity of blue")
for n in range(100):
    led.blue = n/100
    sleep(0.1)
