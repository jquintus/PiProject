import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for pin in range(26):
    print "setting up pin {}".format(pin)
    if pin == 2:
        GPIO.setup(pin, GPIO.IN)
    elif pin == 3:
        GPIO.setup(pin, GPIO.IN)
    else:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Listening for buttons"

while True:
    for pin in range(26):
        input_state = GPIO.input(pin)
        if input_state == GPIO.LOW:
            print("Button pressed")

    time.sleep(0.2)
