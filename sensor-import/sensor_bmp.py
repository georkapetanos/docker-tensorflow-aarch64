#!/usr/bin/python3

from bmp280 import BMP280
from datetime import date
from getmac import get_mac_address
import os
import time
import json

def send_json(time, temp, pressure):
        mac = get_mac_address()
        feature = "2"
        x = '{\n\t\"mac\": \"'+mac+ \
        '\",\n\t\"time\": \"'+time+ \
        '\",\n\t\"feature\": \"'+feature+ \
        '\",\n\t\"temperature\": \"'+temperature+ \
        '\",\n\t\"pressure\": \"'+pressure+ \
        '\"\n}'
        print(x)

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

startdate = date.today().strftime("%Y-%m-%d.log")
f = open(startdate, "a")

while True:
        #check to start logging in a new file
        curdate = date.today().strftime("%Y-%m-%d.log")
        if startdate != curdate:
                print("Logging in a new file...")
                startdate = curdate
                f.close()
                f.open(startdate, "a")

        temperature = "{:.2f}".format(bmp280.get_temperature())
        pressure = "{:.2f}".format(bmp280.get_pressure())
        curtime = time.strftime("%H:%M:%S")
        f.write(curtime+" "+temperature+" "+pressure+"\n")
        print(curtime+" INFO Temp = "+temperature+" C, pressure = "+pressure+" hPa")
        send_json(curtime, temperature, pressure)
        time.sleep(10)

