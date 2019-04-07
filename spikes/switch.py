'''
https://projects.raspberrypi.org/en/projects/physical-computing/9
'''

from gpiozero import LED, Button
from signal import pause

led = LED(23)
button = Button(24)

led.off()

'''
button.when_pressed = led.on 
button.when_released = led.off
'''

def pressed():
    # led.toggle()
    print("pressed")

button.when_pressed = pressed


raw_input("press any key to conitune...")
