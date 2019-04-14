import RPi.GPIO as GPIO

class Button:
    def __init__(self, pin, cmd, noop):
        self.pin = pin
        self.cmd = cmd
        self.noop = noop
        self.state = False

    def setup(self):
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_command(self):
        input_state = GPIO.input(self.pin)

        if input_state == GPIO.LOW:
            if not self.state:
                self.state = True
                return self.cmd
            else:
                return self.noop
        else:
            self.state = False
            return self.noop
