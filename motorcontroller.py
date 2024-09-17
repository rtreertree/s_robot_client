import gpiozero
import time

class MotorController:
    def __init__(self):
        self.motor = gpiozero.Motor(20, 16)

    def forward(self):
        self.motor.forward()

    def backward(self):
        self.motor.backward()

    def stop(self):
        self.motor.stop()


motor = MotorController()
motor.forward()

time.sleep(2)

motor.backward()

time.sleep(2)

motor.stop()

# free resources
motor.motor.close()