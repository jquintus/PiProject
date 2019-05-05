import RPi.GPIO as GPIO
from datetime import datetime, timedelta

class HoldButton:
    def __init__(self, pin, cmd_at_time, cmd_release, noop, timeout):
        self.pin = pin
        self.cmd_at_time = cmd_at_time
        self.cmd_release = cmd_release
        self.noop = noop
        self.timeout = timeout

        self.reset()


    def reset(self):
        self.start_press_time = None
        self.at_time_sent = False


    def setup(self):
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def button_down_delta(self):
        if self.start_press_time:
            now = datetime.now()
            return now - self.start_press_time
        else:
            return timedelta(0)


    def time_up(self):
        delta = self.button_down_delta()
        return delta > self.timeout


    def get_command(self):
        input_state = GPIO.input(self.pin)

        if input_state == GPIO.LOW:
            if not self.start_press_time:
                self.start_press_time = datetime.now()
            
            if self.time_up() and not self.at_time_sent:
                self.at_time_sent = True
                return self.cmd_at_time
            else:
                return self.noop
        else:
            if self.time_up():
                self.reset()
                return self.cmd_release
            else:
                self.reset()
                return self.noop
