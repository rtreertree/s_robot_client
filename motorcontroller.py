import RPi.GPIO as GPIO
import time

IRs = [2, 3, 4, 17, 27]

# ir sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRs, GPIO.IN)

currentSensor = [0, 0, 0, 0, 0]

# while True:
#     for i in range(5):
#         currentSensor[i] = GPIO.input(IRs[i])
#     print(currentSensor)

#     time.sleep(0.5)


# motor
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 1000)
pwm.start(0)

while True:
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)

    pwm.ChangeDutyCycle(75)
    time.sleep(1)