import IR_reader

IRs = [2, 3, 4, 17, 27]

ir_reader = IR_reader.IRSensor(IRs)
sensor = ir_reader.get_sensor()


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
    

print(sensor)
print(get_error())