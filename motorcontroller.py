import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


# create motor class
class Motor:
    def __init__(self, en1, in1, in2):
        self.en1 = en1
        self.in1 = in1
        self.in2 = in2

        GPIO.setup([self.en1, self.in1, self.in2], GPIO.OUT)

        self.pwm = GPIO.PWM(self.en1, 1000)
        self.pwm.start(0)

    def forward(self, speed):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(0)

