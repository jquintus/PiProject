import time
import digitalio
import board
import adafruit_matrixkeypad
import simpleio

cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D10, board.D11, board.D12, board.D13)]
rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D7)]
keys = ((1, 2, 4, 8, 16),
        (32, 64, 128, 256, 512))

# rowsx = [digitalio.DigitalInOut(board.D6)]
# keysx = (("Blue 1", "White 1", "Yellow 1", "Black 1", "Red 1"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


print ("setting up LEDs")

data = digitalio.DigitalInOut(board.D2)
data.direction = digitalio.Direction.OUTPUT
latch = digitalio.DigitalInOut(board.D4)
latch.direction = digitalio.Direction.OUTPUT
clk = digitalio.DigitalInOut(board.D3)
clk.direction = digitalio.Direction.OUTPUT

print ("Start pressing buttons")

while True:
    keys = keypad.pressed_keys
    print("Pressed: ", keys)
    byte = sum(keys)

    # if (last_byte != byte and byte > 0):
    # write to 595 chip
    latch.value = False
    simpleio.shift_out(data, clk, byte, bitcount=10) 
    print("sending: {0:#020b} {0}".format(byte),end="\n")
    latch.value = True
    last_byte = byte

    time.sleep(0.1)



