#!/usr/bin/python3

import pika, sys, os, json

def main():
	credentials = pika.PlainCredentials('admin', '1761856778')
	parameters = pika.ConnectionParameters('192.168.2.101', 5672, '/', credentials)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.queue_declare(queue='sensor')

	# This is executed on every received message, decode and print JSON values
	def callback(ch, method, properties, body):
		#print("\nReceived JSON:\n"+body.decode())
		json_object = json.loads(body.decode())
		temperature = json_object["values"]["temperature"]
		pressure = json_object["values"]["pressure"]
		time = json_object["time"]
		mac = json_object["mac"]
		feature = json_object["feature"]
		print("\nDevice: "+mac+"\n"+time+", "+temperature+" C, "+pressure+" hPa")

	channel.basic_consume(queue='sensor', on_message_callback=callback, auto_ack=True)

	print('Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)
