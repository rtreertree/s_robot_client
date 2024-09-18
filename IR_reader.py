import RPi.GPIO as GPIO
import time

IRs = [2, 3, 4, 17, 27]

class IRSensor:
    def __init__(self, irs:list[int]):
        self.IRs = irs
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IRs, GPIO.IN)
        self.currentSensor = [0, 0, 0, 0, 0]

    def get_sensor(self):
        for i in range(5):
            self.currentSensor[i] = GPIO.input(self.IRs[i])
        return self.currentSensor

if __name__ == '__main__':
    ir_reader = IRSensor(IRs)
    sensor = ir_reader.get_sensor()
    while True:
        print(sensor)
        sensor = ir_reader.get_sensor()
        time.sleep(0.1)