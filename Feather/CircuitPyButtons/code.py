"""
"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

import rotaryio

# Set up constants
VOLUME_UP = 0x80
VOLUME_DOWN = 0x81

# Set up buttons
button_top_red = DigitalInOut(board.D12)
button_top_red.direction = Direction.INPUT
button_top_red.pull = Pull.UP

button_bot_red = DigitalInOut(board.D11)
button_bot_red.direction = Direction.INPUT
button_bot_red.pull = Pull.UP

button_bot_yel = DigitalInOut(board.D10)
button_bot_yel.direction = Direction.INPUT
button_bot_yel.pull = Pull.UP

button_top_yel = DigitalInOut(board.D9)
button_top_yel.direction = Direction.INPUT
button_top_yel.pull = Pull.UP

button_top_blu = DigitalInOut(board.D6)
button_top_blu.direction = Direction.INPUT
button_top_blu.pull = Pull.UP

button_bot_blu = DigitalInOut(board.D5)
button_bot_blu.direction = Direction.INPUT
button_bot_blu.pull = Pull.UP

# Set up rotary encoder
encoder = rotaryio.IncrementalEncoder(board.A1, board.A0)
last_position = encoder.position

# Set up Keyboard and Bluethooth
hid = HIDService()

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CircuitPython HID 2"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)

k = Keyboard(hid.devices)
kl = KeyboardLayoutUS(k)

mouse = Mouse(hid.devices)

# Define some helper functions
def move_mouse_to_right_screen():
    SCREEN_X = 1920 * 2
    SCREEN_Y = 1080 * 2

    """
    MacOS has a concept of "hot corners". A side effect of this is that when
    you move the mouse to the very bottom of the screen and then move the mouse
    horiztonally to the next screen, it will get "stuck" in the bottom corner
    and not move past it, possibly also activating whatever behavior is set up
    for that "hot corner". To avoid this, I'm moving the mouse to the bottom of
    the screen, then up just a little bit to get over the "lip" of the screen.
    Then I move the mouse horizontally to the right screen. 
    
    Trying to do this all in one go would likely result in getting caught in that lip.
    """
    mouse.move(y=SCREEN_Y)
    mouse.move(y=-100)
    mouse.move(x = SCREEN_X)
    mouse.move(x=-100)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.1)

while True:
    while not ble.connected:
        pass
    print("Start typing:")

    while ble.connected:
        if not button_top_red.value:
            print("Button 12 (top red) - Toggle Video")
            move_mouse_to_right_screen()
            k.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)
            time.sleep(0.4)

        if not button_bot_red.value:
            print("Button 11 (bot red) - Toggle Mute")
            move_mouse_to_right_screen()
            k.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
            time.sleep(0.4)

        if not button_top_yel.value:
            print("Button  9 (top yel) - Change View")
            move_mouse_to_right_screen()
            k.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.W)
            time.sleep(0.4)

        if not button_bot_yel.value:
            print("Button 10 (bot yel) - Start Screen Share")
            move_mouse_to_right_screen()
            k.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.S)
            time.sleep(0.1)
            k.send(Keycode.RIGHT_ARROW)
            time.sleep(0.1)
            k.send(Keycode.ENTER)
            time.sleep(0.4)

        if not button_top_blu.value:
            print("Button  6 (top blu) - Start Meeting")
            k.send(Keycode.COMMAND, Keycode.CONTROL, Keycode.V)
            time.sleep(0.4)

        if not button_bot_blu.value:
            print("Button  5 (bot blu) - Closing Meeting")
            move_mouse_to_right_screen()
            k.send(Keycode.COMMAND, Keycode.W)
            time.sleep(0.1)
            k.send(Keycode.ENTER)
            time.sleep(0.4)

        # Rotary encoder (volume knob)
        current_position = encoder.position
        position_change = current_position - last_position
        if position_change > 0:
            for _ in range(position_change):
                print("Going up")
                k.send(VOLUME_UP)
            print(current_position)

        elif position_change < 0:
            for _ in range(-1 * position_change):
                print("going down")
                k.send(VOLUME_DOWN)
            print(current_position)

        last_position = current_position

    ble.start_advertising(advertisement)

