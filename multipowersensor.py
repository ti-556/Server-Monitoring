import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import time
import math

multiplier = 4

#number of CT clamps
sensornum = 4

def calcpower(maxsample):
    
    #set bus for I2C
    i2cbus = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2cbus, address = 0x48)
    
    #ADC conversion mode
    ads.mode = Mode.SINGLE
    
    #data rate for ADC conversion (samples per sec)
    ads.dara_rate = 860
    
    #list of values obtained from CT clamps
    powerlist = []
    
    for channel in range(sensornum):    
        data = 0
        sqvoltsum = 0.0
        voltsum = 0.0
        rms = 0.0
        volt = 0.0
        
        #loop for RMS calculation
        while(data < maxsample):
        
            if channel == 0:
                analogin = AnalogIn(ads, ADS.P0)
            elif channel == 1:
                analogin = AnalogIn(ads, ADS.P1)
            elif channel == 2:
                analogin = AnalogIn(ads, ADS.P2)
            elif channel == 3:
                analogin = AnalogIn(ads, ADS.P3)
                
            #obtain voltage from CT clamp
            volt = abs(analogin.voltage * multiplier)
            
            #sum of voltage and voltage squared
            voltsum = voltsum + volt
            sqvoltsum = sqvoltsum + volt ** 2
            
            data = data + 1
            
            #calculate average output voltage and RMS from "maxsample" number of voltage data
            avgvolt = voltsum/data
            rms = math.sqrt(sqvoltsum / data)
        
        #calculate current, then power consumption
        amp = rms * 3000 / 1000
        watt = amp * 100
        
        powerlist.append(rms)
        powerlist.append(avgvolt)
        powerlist.append(watt)
        
    return powerlist
        
    

        
        
