import IR_reader
import motorcontroller

IRs = [2, 3, 4, 17, 27]

ir_reader = IR_reader.IRSensor(IRs)
sensor = ir_reader.get_sensor()

motorL = motorcontroller.Motor(26, 19, 13)
motorR = motorcontroller.Motor(6, 5, 12)

def get_error():
    if (sensor[0] == 1 and sensor[1] == 0):
        return -4
    elif (sensor[0] == 1 and sensor[1] == 1):
        return -3
    elif (sensor[1] == 1):
        return -2
    elif (sensor[1] == 1 and sensor[2] == 1):
        return -1
    elif (sensor[2] == 1):
        return 0
    elif (sensor[2] == 1 and sensor[3] == 1):
        return 1
    elif (sensor[3] == 1):
        return 2
    elif (sensor[3] == 1 and sensor[4] == 1):
        return 3
    elif (sensor[4] == 1):
        return 4


while True:
    error = get_error()
    if error == 0:
        motorL.forward(50)
        motorR.forward(50)
    elif error == -4:
        motorL.forward(50)
        motorR.forward(0)
    elif error == 4:
        motorL.forward(0)
        motorR.forward(50)
    elif error == -3:
        motorL.forward(50)
        motorR.forward(25)
    elif error == 3:
        motorL.forward(25)
        motorR.forward(50)
    elif error == -2:
        motorL.forward(50)
        motorR.forward(37.5)
    elif error == 2:
        motorL.forward(37.5)
        motorR.forward(50)
    elif error == -1:
        motorL.forward(50)
        motorR.forward(43.75)
    elif error == 1:
        motorL.forward(43.75)
        motorR.forward(50)
    else:
        motorL.forward(50)
        motorR.forward(50)

    sensor = ir_reader.get_sensor()