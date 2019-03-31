'''
https://projects.raspberrypi.org/en/projects/physical-computing/9
'''

from gpiozero import LED, Button
from signal import pause

led = LED(12)
button = Button(23)

led.off()

'''
button.when_pressed = led.on 
button.when_released = led.off
'''

button.when_pressed = led.toggle 

pause()
