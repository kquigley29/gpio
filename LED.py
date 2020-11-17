import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin):
        self.pin = pin
        self.on = 0

        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, self.on)

    def switch(self, value=-1):
        assert value in [-1, 0, 1], "Value must be -1, 0 or 1."
        if value == -1:
            self.on = not self.on
        elif value in [0, 1]:
            self.on = value
        GPIO.output(self.pin, self.on)
