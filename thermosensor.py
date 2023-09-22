from w1thermsensor import W1ThermSensor
import time

def calctemp():
    #list of sensor ID and it's temperature
    templist = []
    for sensor in W1ThermSensor.get_available_sensors():
        templist.append(sensor.id)
        templist.append(sensor.get_temperature())
    return templist

