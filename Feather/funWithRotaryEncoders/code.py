import rotaryio
import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("finished imports")

button = digitalio.DigitalInOut(board.D9)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D8)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D7)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.D11, board.D10)

cc = ConsumerControl(usb_hid.devices)

button1_state = None
button2_state = None
button3_state = None
last_position = encoder.position

def volume_up(delta):
    for _ in range(delta):
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)

def volume_down(delta):
    for _ in range(-1 * delta):
        print("going down")
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)

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

    if not button.value and button1_state is None:
        button1_state = "pressed"
    if button.value and button1_state == "pressed":
        print("Button 1 pressed.")
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        button1_state = None

    if not button2.value and button2_state is None:
        button2_state = "pressed"
    if button2.value and button2_state == "pressed":
        print("Button 2 pressed.")
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        button2_state = None

    if not button3.value and button3_state is None:
        button3_state = "pressed"
    if button3.value and button3_state == "pressed":
        print("Button 3 pressed.")
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        button3_state = None
