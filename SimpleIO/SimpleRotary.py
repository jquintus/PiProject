'''
Simple code showing off how to use a rotary encoder

Resources:
https://github.com/simonmonk/raspberrypi_cookbook_ed2/blob/master/rotary_encoder.py
https://learning.oreilly.com/library/view/custom-raspberry-pi/9781484224069/A432417_1_En_8_Chapter.html
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set up the push button
buttonPin = 26
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the encoder pins
input_a = 20
input_b = 21

GPIO.setup(input_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(input_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

old_a = True
old_b = True

def get_encoder_turn():
    # return -1, 0, or +1
    result = 0
    global old_a, old_b
    new_a = GPIO.input(input_a)
    new_b = GPIO.input(input_b)

    if new_a != old_a or new_b != old_b:
        if old_a == 0 and new_a == 1:
            result = (old_b * 2 - 1)
        elif old_b == 0 and new_b == 1:
            result = -(old_a * 2 - 1)

    old_a, old_b = new_a, new_b

    return result

def get_button_state():
    input_state = GPIO.input(buttonPin)
    return input_state == GPIO.LOW

counter = 0
old_counter = 0
while True:
    change = get_encoder_turn()
    counter += change 

    if get_button_state():
        counter = 100

    if counter != old_counter:
        print(counter)

    old_counter = counter
    time.sleep(0.001)

