import smbus
import time
import sys
from pynput import keyboard

# defining adresses of each register pin
channel = 1
i2caddr = 0x20
reg_iodira = 0x00
reg_iodirb = 0x01
reg_ipola = 0x02
reg_ipolb = 0x03
reg_gppua = 0x0c
reg_gppub = 0x0d
reg_olata = 0x14
reg_olatb = 0x15

bus = smbus.SMBus(channel)

#reset all pins
bus.write_byte_data(i2caddr, reg_olata, 0x00)
bus.write_byte_data(i2caddr, reg_olatb, 0x00)

bus.write_byte_data(i2caddr, reg_ipola, 0x00)
bus.write_byte_data(i2caddr, reg_ipolb, 0x00)

# pullup off for all GPA and GPB pins
bus.write_byte_data(i2caddr, reg_gppua, 0x00)
bus.write_byte_data(i2caddr, reg_gppub, 0x00)

# set all GPA and GPB pins to output
bus.write_byte_data(i2caddr, reg_iodirb, 0x00)
bus.write_byte_data(i2caddr, reg_iodira, 0x00)

# set a specific GPA pin to high while keeping others low
def turnongpa(binarynum):
    hexnum = int(hex(binarynum), 0)
    bus.write_byte_data(i2caddr, reg_olata, hexnum)

# set all GPA pins to low
def turnoffgpa():
    bus.write_byte_data(i2caddr, reg_olata, 0x00)

# set a specific GPB pin to high while keeping others low
def turnongpb(binarynum):
    hexnum = int(hex(binarynum), 0)
    bus.write_byte_data(i2caddr, reg_olatb, hexnum)

# set all GPB pins to low
def turnoffgpb():
    bus.write_byte_data(i2caddr, reg_olatb, 0x00)

# function to check if all the relays are working
def test():
    turnongpa(0b00000001)
    time.sleep(0.5)
    turnongpa(0b00000010)
    time.sleep(0.5)
    turnongpa(0b00000100)
    time.sleep(0.5)
    turnongpa(0b00001000)
    time.sleep(0.5)
    turnongpa(0b00010000)
    time.sleep(0.5)
    turnongpa(0b00100000)
    time.sleep(0.5)
    turnongpa(0b01000000)
    time.sleep(0.5)
    turnongpa(0b10000000)
    time.sleep(0.5)
    turnoffgpa()
    
    turnongpb(0b00000001)
    time.sleep(0.5)
    turnongpb(0b00000010)
    time.sleep(0.5)
    turnongpb(0b00000100)
    time.sleep(0.5)
    turnongpb(0b00001000)
    time.sleep(0.5)
    turnongpb(0b00010000)
    time.sleep(0.5)
    turnongpb(0b00100000)
    time.sleep(0.5)
    turnongpb(0b01000000)
    time.sleep(0.5)
    turnongpb(0b10000000)
    time.sleep(0.5)
    turnoffgpb()
    
"""
using command line arguments to control relays
format: python3 multirelay.py <on/off> <1~16>
Branching else if for each relay ID since these integers don't correspond to the binary input of the IO expander
"""
if __name__ == "__main__":
    if sys.argv[1] == "on" or sys.argv[1] == "ON":
        if sys.argv[2] == "1":
            turnongpa(0b00000001)
        elif sys.argv[2] == "2":
            turnongpa(0b00000010)
        elif sys.argv[2] == "3":
            turnongpa(0b00000100)
        elif sys.argv[2] == "4":
            turnongpa(0b00001000)
        elif sys.argv[2] == "5":
            turnongpa(0b00010000)
        elif sys.argv[2] == "6":
            turnongpa(0b00100000)
        elif sys.argv[2] == "7":
            turnongpa(0b01000000)
        elif sys.argv[2] == "8":
            turnongpa(0b10000000)
        elif sys.argv[2] == "9":
            turnongpb(0b00000001)
        elif sys.argv[2] == "10":
            turnongpb(0b00000010)
        elif sys.argv[2] == "11":
            turnongpb(0b00000100)
        elif sys.argv[2] == "12":
            turnongpb(0b00001000)
        elif sys.argv[2] == "13":
            turnongpb(0b00010000)
        elif sys.argv[2] == "14":
            turnongpb(0b00100000)
        elif sys.argv[2] == "15":
            turnongpb(0b01000000)
        elif sys.argv[2] == "16":
            turnongpb(0b10000000)
    elif sys.argv[1] == "off" or sys.argv[1] == "OFF":
        turnoffgpa()
        turnoffgpb()
    elif sys.argv[1] == "test" or sys.argv[1] == "TEST":
        test()
        
