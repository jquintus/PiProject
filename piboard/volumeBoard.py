#!/usr/bin/python3
'''
Simple code showing off how to use a rotary encoder

Resources:
https://github.com/simonmonk/raspberrypi_cookbook_ed2/blob/master/rotary_encoder.py
https://learning.oreilly.com/library/view/custom-raspberry-pi/9781484224069/A432417_1_En_8_Chapter.html
'''
import RPi.GPIO as GPIO
import time
from enum import IntEnum

class Cmd(IntEnum):
    NoOp = 0
    VolumeUp = 1
    VolumeDown = 2
    Mute = 3

class Encoder:
    def __init__(self, a_pin, b_pin):
        self.a_pin = a_pin
        self.b_pin = b_pin

        self.old_a = True
        self.old_b = True

    def setup(self):
        GPIO.setup(self.a_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.b_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_encoder_turn(self):
        # return -1, 0, or +1
        result = 0
        self.new_a = GPIO.input(self.a_pin)
        self.new_b = GPIO.input(self.b_pin)

        if self.new_a != self.old_a or self.new_b != self.old_b:
            if self.old_a == 0 and self.new_a == 1:
                result = (self.old_b * 2 - 1)
            elif self.old_b == 0 and self.new_b == 1:
                result = -(self.old_a * 2 - 1)

        self.old_a, self.old_b = self.new_a, self.new_b

        return result

    def get_command(self):
        change = self.get_encoder_turn()
        if change > 0:
            return Cmd.VolumeUp
        elif change < 0:
            return Cmd.VolumeDown
        else:
            return Cmd.NoOp


GPIO.setmode(GPIO.BCM)
# Set up the push button
buttonPin = 26
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_button_cmd(cmd_if_pressed):
    input_state = GPIO.input(buttonPin)
    if input_state == GPIO.LOW:
        return cmd_if_pressed
    else:
        return Cmd.NoOp

def get_command(encoder):
    encoder_cmd = encoder.get_command()
    button_cmd =  get_button_cmd(Cmd.Mute)

    time.sleep(0.001)
    return max([encoder_cmd, button_cmd])

def main():
    encoder = Encoder(20, 21)
    encoder.setup()

    while True:
        command = get_command(encoder)
        if command != Cmd.NoOp:
            print(command)

main()
