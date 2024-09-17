import RPi.GPIO as GPIO
import time

IRs = [2, 3, 4, 17, 27]

# ir sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRs, GPIO.IN)

currentSensor = [0, 0, 0, 0, 0]

while True:
    for i in range(5):
        currentSensor[i] = GPIO.input(IRs[i])
    print(currentSensor)

    time.sleep(0.5)