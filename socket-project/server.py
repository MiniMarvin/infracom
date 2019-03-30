#!/usr/bin/env python3
"""
Server for file transference
"""

import sys
import socket
from socket import socket as Socket

def main():
    """
    Main loop for the python server
    """
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
            print("======================")


    return 0


def http_handle(request, data_socket):
    """Given a http requst return a response
    Both request and response are unicode strings with platform standard
    line endings.

    Adopted protocol:
    << COMMAND NAME >>||<< FILENAME >>[||<< DATA >>]
    """
    request_string = request.decode()
    parts = request_string.split("||")
    command = parts[0]
    filename = parts[1]


    ## If it is binary it will receive the file
    if command == "POST":
        num = len(command) + 3 + len(filename) + 1

        with open(filename, "wb") as file:
            data = request[num:]
            while data:
                file.write(data)
                data = data_socket.recv(1024)
        return "OK".encode()

    ## Otherwise it will send a file
    elif command == "GET":
        # n = len(command) + 1
        contents = ''
        with open(filename, 'rb') as file:
            contents = file.read()
        return contents

    return "ERR".encode()

if __name__ == "__main__":
    sys.exit(main())
