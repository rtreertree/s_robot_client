import RPi.GPIO as GPIO
import time


# ir sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)


while True:
    if GPIO.input(2):
        print("Obstacle detected")
    else:
        print("No obstacle detected")
    time.sleep(1)