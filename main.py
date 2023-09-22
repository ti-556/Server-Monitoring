
import threading
import time
from multipowersensor import calcpower
from thermosensor import calctemp
from webcamcapture import capture
from prometheus_client import start_http_server, Gauge

#trialnum is the number of voltage data for rms calculation 
trialnum = 50

#start HTTP server of exporter on port 8000
start_http_server(8000)

#setting gauge type metric for each variable (temperature, voltage, and power)
t1 = Gauge("T1:", "Temperature of Sensor 1 in Celsius")
t2 = Gauge("T2:", "Temperature of Sensor 2 in Celsius")
t3 = Gauge("T3:", "Temperature of Sensor 3 in Celsius")
t4 = Gauge("T4:", "Temperature of Sensor 4 in Celsius")

v1 = Gauge("V1:", "Voltage of Sensor 1 in Volts")
v2 = Gauge("V2:", "Voltage of Sensor 2 in Volts")
v3 = Gauge("V3:", "Voltage of Sensor 3 in Volts")
v4 = Gauge("V4:", "Voltage of Sensor 4 in Volts")

p1 = Gauge("P1:", "Power of Sensor 1 in Watts")
p2 = Gauge("P2:", "Power of Sensor 2 in Watts")
p3 = Gauge("P3:", "Power of Sensor 3 in Watts")
p4 = Gauge("P4:", "Power of Sensor 4 in Watts")

#calculate sensor output voltage and power consumption from CT clamp
def powercalculation():
    while(True):
        #list of values obtained from CT clamp
        powerresult = calcpower(trialnum)
        
        #set metric values for voltage
        v1.set(powerresult[1])
        v2.set(powerresult[4])
        v3.set(powerresult[7])
        v4.set(powerresult[10])
        
        #set metric values for power
        p1.set(powerresult[2])
        p2.set(powerresult[5])
        p3.set(powerresult[8])
        p4.set(powerresult[11])
        
        print("volt & power updated")

#calculate temperature from 1-wire thermosensor
def temperaturecalculation():
    while(True):
        time.sleep(3)
        #list of values obtained from thermosensor
        tempresult = calctemp()
        
        #set metric values for temperature
        t1.set(tempresult[1])
        t2.set(tempresult[3])
        t3.set(tempresult[5])
        t4.set(tempresult[7])
        
        print("temperature updated")

#multithreading loops 
powerthread = threading.Thread(target = powercalculation)
tempthread = threading.Thread(target = temperaturecalculation)
webcamthread = threading.Thread(target = capture)

powerthread.start()
tempthread.start()
webcamthread.start()


            
