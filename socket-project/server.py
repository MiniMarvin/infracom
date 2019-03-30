#!/usr/bin/env python3

import sys
import itertools
import socket
from socket import socket as Socket


def main():

	# Create the server socket (to handle tcp requests using ipv4), make sure
	# it is always closed by using with statement.
	with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

		# The socket stays connected even after this script ends. So in order
		# to allow the immediate reuse of the socket (so that we can kill and
		# re-run the server while debugging) we set the following option. This
		# is potentially dangerous in real code: in rare cases you may get junk
		# data arriving at the socket.
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		server_socket.bind(('', 2080))
		server_socket.listen(1)

		print("server ready")

		while True:
			
			with server_socket.accept()[0] as connection_socket:
				request = connection_socket.recv(1024)
				reply = http_handle(request, connection_socket)
				connection_socket.send(reply)
			

			print("\n\nReceived request")
			print("======================")
			print(request.rstrip())
			print("======================")


			print("\n\nReplied with")
			print("======================")
			print(reply)
			# print(reply.rstrip())
			print("======================")


	return 0


def http_handle(request, socket):
	"""Given a http requst return a response
	Both request and response are unicode strings with platform standard
	line endings.
	
		Adopted protocol:
		<< COMMAND NAME >>||<< FILENAME >>[||<< DATA >>]
	"""
	request_string = request.decode()
	# print('request: ' + request_string)
	
	parts = request_string.split("||")
	command = parts[0]
	filename = parts[1]

	
	## If it is binary it will receive the file
	if command == "POST":
		## TODO: Update to support image partitioning
		n = len(command) + 3 + len(filename) + 1
		
		## TODO: verify if file exists
		with open(filename, "wb") as f:
			data = request[n:]
			while data:
				f.write(data)
				data = socket.recv(1024)
				# data = data[n:]  
				## Ignore anything after that

		return "OK".encode()
	
	## Otherwise it will send a file
	elif command == "GET":
		n = len(command) + 1
		contents = ''
		with open(filename, 'rb') as file:
			contents = file.read()
		return contents
	
	return "ERR".encode()

if __name__ == "__main__":
	sys.exit(main())