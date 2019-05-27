import board
import busio
import digitalio
import adafruit_tlc59711

def create_spi():
    spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
    return spi

class RgbLed:

    def __init__(self, spi):
        self.spi = spi
        self.MAX = 65535
        self.MAX_BRIGHT = 127

    def setup(self):
        self.led = adafruit_tlc59711.TLC59711(self.spi)


    def get_command(self):
        pass


    def red(self, idx):
       self.led[idx] =  (self.MAX, 0, 0)


    def green(self, idx):
       self.led[idx] =  (0, self.MAX, 0)


    def blue(self, idx):
       self.led[idx] =  (0, 0, self.MAX)


    def purple(self, idx):
        red = int(self.MAX / 4)
        self.led[idx] = (red, 0, self.MAX)


    def dim(self):
        self.led.red_brightness = 6
        self.led.green_brightness = 6
        self.led.bluebrightness = 6

