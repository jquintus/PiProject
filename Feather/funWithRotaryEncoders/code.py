import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import rotaryio
import board
import digitalio

"""
HARDWARE
Board: Metro Express
Rotary encoder
    clk   -> D11
    dt    -> D10
    sw    -> D9
    +     -> 5v
    grnd  -> grnd

STEMMA Wired Tactile Push-Button Pack
    Red Button   -> GRND & D8
    Black Button -> GRND & D7
"""

print("finished imports")

VOLUME_UP = 0x80
VOLUME_DOWN = 0x81

hid = HIDService()

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "TEST CircuitPython HID"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)

k = Keyboard(hid.devices)
kl = KeyboardLayoutUS(k)

encoder = rotaryio.IncrementalEncoder(board.A1, board.A2)
last_position = encoder.position

def volume_up(delta):
    for _ in range(delta):
        print("Going up")
        k.send(VOLUME_UP)

def volume_down(delta):
    for _ in range(-1 * delta):
        print("going down")
        k.send(VOLUME_DOWN)

print("Finished setup")
while True:
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        volume_up(position_change)
        print(current_position)
    elif position_change < 0:
        volume_down(position_change)
        print(current_position)
    last_position = current_position
