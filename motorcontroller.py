import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 1000)

pwm.start(0)

while True:
    GPIO.output(19, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)