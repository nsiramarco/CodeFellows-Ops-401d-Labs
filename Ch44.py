#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = # TODO: Collect a host IP from the user.
portno = # TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(port)


# Resources
#          Python socket module documentation - https://docs.python.org/3/library/socket.html
#          DEMO.md - https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html
