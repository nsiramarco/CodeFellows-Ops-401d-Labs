#!/usr/bin/env python3
import os
from scapy.all import srl, IP, ICMP, TCP # scapy library


# Script Name:                  Network Security Tool with Scapy Part 1 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/25/2023
# Purpose:                      In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
#                               
#                               Utilize the scapy library
#                               Define host IP
#                               Define port range or specific set of ports to scan
#                               Test each port in the specified range using a for loop
#                               If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#                               If flag 0x14 received, notify user the port is closed.
#                               If no flag is received, notify the user the port is filtered and silently dropped.


# Function
# Assited with class video
# Define Host
host = "scanme.nmap.org"
#Port Range
port_range = 22
port_scan = 22
port_dest = 22

# Ping Ports
ping = srl(IP(dst = host)/ICMP())
if ping:
    ping.show()

# TCP packet

response = srl(IP(dst = host)/TCP(sport = port_scan, dport = port_dest, flags = "S"), timeout = 1, verbose = 0)

if (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
              # Send RST packet
              send_rst = srl(IP(dst = host)/TCP(sport = port_scan, dport = port_dest, flags = "R"), timeout = 1, verbose = 0)
              print (f"{host}:{port_dest} is open.")
        elif (response.getlayer(TCP).flags == 0x14):
              # Notify its closed
              print (f"{host}:{port_dest} is closed.")
        elif (response.getlayer(TCP).flags == 0x14):  # need to fix
              # Notify No FLag
              print (f"{host}:{port_dest} port is filtered and silently dropped")
else:
      print("Host in unresponsive.")
# Main

# End

#       Resources
#           [Scapy Official Documentation](https://scapy.readthedocs.io/en/latest/index.html)
#           [About Scapy](https://scapy.readthedocs.io/en/latest/introduction.html#)
#           [Build your own tools](https://scapy.readthedocs.io/en/latest/extending.html)