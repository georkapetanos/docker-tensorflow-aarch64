#!/usr/bin/python3

from bmp280 import BMP280
from datetime import date
from getmac import get_mac_address
import os
import time
import json
import pika
import yaml

def get_readings():
	#read data from sensors
	temperature = "{:.2f}".format(bmp280.get_temperature())
	pressure = "{:.2f}".format(bmp280.get_pressure())
	curtime = time.strftime("%H:%M:%S")

	return curtime, temperature, pressure

def log_local(f, curtime, temperature, pressure):
	#log data on local consol and file
	#check to start logging in a new file every day
	curdate = date.today().strftime("%Y-%m-%d.log")
	global startdate
	if startdate != curdate:
		print("Logging in a new file...")
		startdate = curdate
		f.close()
		f.open(startdate, "a")

	f.write(curtime+" "+temperature+" "+pressure+"\n")
	f.flush()
	print(curtime+" INFO Temp = "+temperature+" C, pressure = "+pressure+" hPa")

def send_json(time, temp, pressure):
	#send data to mqtt broker in JSON format
	mac = get_mac_address()
	feature = "2"
	message = '{\n\t\"mac\": \"'+mac+ \
	'\",\n\t\"time\": \"'+time+ \
	'\",\n\t\"feature\": \"'+feature+ \
	'\",\n\t\"values\": {'+ \
	'\n\t\t\"temperature\": \"'+temperature+ \
	'\",\n\t\t\"pressure\": \"'+pressure+ \
	'\"\n\t}\n}'
	print(message)

	# publish sensor data to MQTT server
	global username, password, ip, port

	credentials = pika.PlainCredentials(username, password)
	parameters = pika.ConnectionParameters(ip, port, '/', credentials)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.queue_declare(queue='sensor')
	channel.basic_publish(exchange='', routing_key='sensor', body=message)
	connection.close()

try:
	from smbus2 import SMBus
except ImportError:
	from smbus import SMBus

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

global startdate, username, password, ip, port
# open log file with date as name
startdate = date.today().strftime("%Y-%m-%d.log")
f = open(startdate, "a")

# open config file located in the same directory
config = open('config.yaml', 'r')
doc = yaml.load(config, Loader=yaml.SafeLoader)

# load YAML values from config, password and port
# are currently set as int values
username = doc["username"]
password = str(doc["password"])
ip = doc["MQserver"]
port = str(doc["port"])

while True:
	curtime, temperature, pressure = get_readings()

	log_local(f, curtime, temperature, pressure)

	send_json(curtime, temperature, pressure)

	time.sleep(10)
