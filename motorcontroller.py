import gpiozero
import time


motor = gpiozero.Motor(20, 16)
motor.forward()
time.sleep(2)
motor.stop()
time.sleep(2)
motor.close()