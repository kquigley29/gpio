import RPi.GPIO as GPIO
import time


class Stepper:
    def __init__(self, pins, wait=0.001):
        self.pins = pins
        self.wait = wait

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        self.halfstep_seq = [[1, 0, 0, 0],
                             [1, 1, 0, 0],
                             [0, 1, 0, 0],
                             [0, 1, 1, 0],
                             [0, 0, 1, 0],
                             [0, 0, 1, 1],
                             [0, 0, 0, 1],
                             [1, 0, 0, 1]]

    def rotate(self, direction):
        assert direction == 1 or direction == -1, "Direction must be 1 (.), or -1 (x)"
        for halfstep in range(len(self.halfstep_seq)):
            for pin in range(len(self.pins)):
                GPIO.output(self.pins[pin], self.halfstep_seq[halfstep][(direction * pin) % 4])
            time.sleep(self.wait)
