import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 26
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Listening for buttons"

while True:
    input_state = GPIO.input(pin)
    if input_state == GPIO.LOW:
        print("Button pressed")

    time.sleep(0.2)
