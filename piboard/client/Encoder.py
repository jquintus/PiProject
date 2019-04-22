import RPi.GPIO as GPIO

class Encoder:
    def __init__(self, a_pin, a_cmd, b_pin, b_cmd, noop):
        self.a_pin = a_pin
        self.a_cmd = a_cmd

        self.b_pin = b_pin
        self.b_cmd = b_cmd
        self.noop = noop

        self.old_a = True
        self.old_b = True

    def setup(self):
        GPIO.setup(self.a_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.b_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_encoder_turn(self):
        # return -1, 0, or +1
        result = 0
        self.new_a = GPIO.input(self.a_pin)
        self.new_b = GPIO.input(self.b_pin)

        if self.new_a != self.old_a or self.new_b != self.old_b:
            if self.old_a == 0 and self.new_a == 1:
                result = (self.old_b * 2 - 1)
            elif self.old_b == 0 and self.new_b == 1:
                result = -(self.old_a * 2 - 1)

        self.old_a, self.old_b = self.new_a, self.new_b

        return result

    def get_command(self):
        change = self.get_encoder_turn()
        if change > 0:
            return self.a_cmd
        elif change < 0:
            return self.b_cmd
        else:
            return self.noop
