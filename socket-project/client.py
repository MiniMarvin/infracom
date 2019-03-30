#!/usr/bin/env python3
"""
Client for file transference
"""


import socket
import argparse
import subprocess
import os


def get_file():
    """
    Get a file from the server
    """
    sentence = ARGS.file
    outfile = ARGS.output
    CLIENT_SOCKET.send("GET||".encode() + sentence.encode())

    with open(outfile, "wb") as file:
        data = CLIENT_SOCKET.recv(1024)
        while data:
            file.write(data)
            data = CLIENT_SOCKET.recv(1024)

    CLIENT_SOCKET.close()

def get_prog_file():
    """
    Get a binary file from the server and runs it automatically
    """
    get_file()
    ## Executa
    file = ARGS.output
    os.system("chmod +x " + file)
    subprocess.call([file])


def send_file():
    """
    Send a file to the server
    """
    data = ARGS.data
    filename = ARGS.file
    outstream = "POST||" + filename + "||" + data
    CLIENT_SOCKET.send(outstream.encode())


SERVER_NAME = "localhost"
SERVER_PORT = 2080

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PARSER = argparse.ArgumentParser()
PARSER.add_argument("--command", "-c", type=str,
                    help="GET file filename | to get a file from the server")
PARSER.add_argument('--file', '-f', type=str,
                    help='File to get from server')
PARSER.add_argument('--output', '-o', type=str,
                    help='Output file name for get')
PARSER.add_argument('--data', '-d', type=str,
                    help='Output file data for post')
ARGS = PARSER.parse_args()

try:
    CLIENT_SOCKET.connect((SERVER_NAME, SERVER_PORT))
except Exception:
    pass

try:
    if ARGS.command.upper() == "GET":
        get_file()

    elif ARGS.command.upper() == "GETPROG":
        get_prog_file()

    elif ARGS.command.upper() == "POST":
        send_file()

except KeyboardInterrupt:
    # escape = True
    pass
except Exception:
    CLIENT_SOCKET.close()


CLIENT_SOCKET.close()
print("\nBye bye :)")
