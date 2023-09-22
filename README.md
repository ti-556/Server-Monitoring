# monitoring

## Setup
Enable 1-Wire interface by adding the following line on config.txt, then reboot raspi.
```
$ sudo nano /boot/config.txt
[all]
dtoverlay=w1-gpio,pullup=on
$ reboot
```

## Libraries
```
pip3 install threading
pip3 install cv2
pip3 install adafruit-blinka
pip3 install w1thermsensor
pip3 install prometheus_client
pip3 install adafruit-circuitpython-ads1x15
```

## Circuit

![circuit diagram](thermopowercircuit.png)

![pcb layout](thermopowerpcb.png)

![pcb 3d  model](thermopowerpcb3d.png)


