#!/usr/bin/python3

import socket
import time

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = time.sleep(15)
sockmod.settimeout(timeout)

hostip = input("Enter Host Ip Address: ")
portno = int(input("Enter Port Number: "))

def portScanner(portno):
    if sockmod.connect((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)


# Resources
#          Python socket module documentation - https://docs.python.org/3/library/socket.html
#          DEMO.md - https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html
