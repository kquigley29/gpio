import RPi.GPIO as GPIO


class Button:
    def __init__(self, pin):
        self.pressed = False
        self.released = False
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def press(self):
        value = GPIO.input(self.pin) == GPIO.HIGH
        if self.pressed and not value:
            self.released = True

        elif self.released and value:
            self.pressed = False

        self.pressed = value

    def is_pressed(self):
        return self.pressed

    def is_released(self):
        r = self.released
        self.released = False
        return r

    def check_in_thread(self):
        while True:
            self.press()
