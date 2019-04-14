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
from Encoder import Encoder
from Button import Button

class Cmd(IntEnum):
    NoOp = 0
    VolumeUp = 1
    VolumeDown = 2
    Mute = 3

def get_command(inputs):
    cmd = max(list(map(lambda i: i.get_command(), inputs)))
    time.sleep(0.001)
    return cmd

def main():
    GPIO.setmode(GPIO.BCM)

    inputs = [
        Encoder(20, Cmd.VolumeDown, 21, Cmd.VolumeUp, Cmd.NoOp),
        Button(26, Cmd.Mute, Cmd.NoOp)
    ]
    list(map(lambda i: i.setup(), inputs))

    actions = {
        Cmd.VolumeUp: lambda: print ("up"),
        Cmd.VolumeDown: lambda: print ("down"),
        Cmd.Mute: lambda: print ("mute"),
    }

    while True:
        command = get_command(inputs)
        action = actions.get(command, lambda: None)
        action()

main()
