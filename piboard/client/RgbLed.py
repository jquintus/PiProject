import board
import busio
import digitalio
import adafruit_tlc59711

class RgbLed:
    MAX = 65535
    MAX_BRIGHT = 127


    def create_spi():
        self.led = adafruit_tlc59711.TLC59711(spi)


    def __init__(self, spi)
        self.spi = spi


    def setup(self):
        self.led = adafruit_tlc59711.TLC59711(spi)


    def get_command(self):
        pass


    def red(self, idx):
       self.led[idx] =  (MAX, 0, 0)


    def green(self, idx):
       self.led[idx] =  (0, MAX, 0)


    def blue(self, idx):
       self.led[idx] =  (0, 0, MAX)

