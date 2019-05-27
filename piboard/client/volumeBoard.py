#!/usr/bin/python3
'''
Simple code showing off how to use a rotary encoder

Resources:
https://github.com/simonmonk/raspberrypi_cookbook_ed2/blob/master/rotary_encoder.py
https://learning.oreilly.com/library/view/custom-raspberry-pi/9781484224069/A432417_1_En_8_Chapter.html
https://learn.adafruit.com/tlc5947-tlc59711-pwm-led-driver-breakout/python-circuitpython
'''
import RPi.GPIO as GPIO
import time
from datetime import timedelta
from enum import IntEnum
from Encoder import Encoder
from Button import Button
from HoldButton import HoldButton
import RgbLed
import requests
import os

class Cmd(IntEnum):
    NoOp = 0
    VolumeUp = 1
    VolumeDown = 2
    Mute = 3
    ShutdownHeld = 4
    Shutdown = 5


def get_command(inputs):
    cmd = max(list(map(lambda i: i.get_command(), inputs)))
    time.sleep(0.001)
    return cmd


def fire_and_forget(url):
    def fire():
        requests.get(url)

    fire()


def shutdown(rgb):
    os.system("sudo poweroff")


def create_actions(rgb):
    url = "https://webhook.site/c533e505-2b6d-418b-980f-9742f9009fab/"
    url = "http://surface3:5000/"
    actions = {
        Cmd.VolumeUp: lambda: fire_and_forget(url + "up"),
        Cmd.VolumeDown: lambda: fire_and_forget(url + "down"),
        Cmd.Mute: lambda: fire_and_forget(url + "mute"),
        Cmd.ShutdownHeld: lambda: rgb.red(1),
        Cmd.Shutdown: lambda: shutdown(rgb)
    }

    return actions

def initialize_led():
    spi = RgbLed.create_spi()
    rgb = RgbLed.RgbLed(spi)
    rgb.setup();
    rgb.green(1)
    return rgb


def main(actions):

    GPIO.setmode(GPIO.BCM)

    inputs = [
        Encoder(20, Cmd.VolumeDown, 21, Cmd.VolumeUp, Cmd.NoOp),
        Button(26, Cmd.Mute, Cmd.NoOp),
        HoldButton(3, Cmd.NoOp, Cmd.Shutdown, Cmd.NoOp, timedelta(0,3)),
    ]

    list(map(lambda i: i.setup(), inputs))

    while True:
        command = get_command(inputs)
        action = actions.get(command, lambda: None)
        action()


def test_inputs():
    GPIO.setmode(GPIO.BCM)

    hb = HoldButton(13, "held", "released", None, timedelta(0, 2))
    hb.setup()
    inputs = [hb]

    print ("start pressing")
    while True:
        command = get_command(inputs)
        if command:
            print(command)


rgb = initialize_led()
actions = create_actions(rgb)
main(actions)
