#!/usr/bin/env python3

import socket
import argparse
import subprocess
import os


def getFile():
	sentence = args.file
	outfile = args.output
	clientSocket.send("GET||".encode() + sentence.encode())
	
	with open(outfile, "wb") as f:
		data = clientSocket.recv(1024)
		while data:
			f.write(data)
			data = clientSocket.recv(1024)
	
	clientSocket.close()
	pass

def getProgFile():
	getFile()
	## Executa
	file = args.output
	os.system("chmod +x " + file)
	subprocess.call([file])
	

def sendFile():
	data = args.data
	filename = args.file
	outstream = "POST||" + filename + "||" + data
	clientSocket.send(outstream.encode())
	pass
	

serverName = "localhost"
serverPort = 2080

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument("--command", "-c", type=str,
					help="GET file filename | to get a file from the server")
parser.add_argument('--file', '-f', type=str,
					help='File to get from server')
parser.add_argument('--output', '-o', type=str,
					help='Output file name for get')
parser.add_argument('--data', '-d', type=str,
					help='Output file data for post')
args = parser.parse_args()

try:
	clientSocket.connect((serverName,serverPort))
except Exception:
	pass

try:
	if args.command == "GET":
		getFile()
	
	elif args.command == "GETPROG":
		getProgFile()
		
	elif args.command == "POST":
		sendFile()

except KeyboardInterrupt:
	escape = True
except Exception:
	clientSocket.close()


clientSocket.close()
print("\nBye bye :)")