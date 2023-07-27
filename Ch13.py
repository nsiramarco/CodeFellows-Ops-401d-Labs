#!/usr/bin/env python3
import ipaddress
from scapy.all import IP, ICMP, TCP, sr1


# Script Name:                  Network Security Tool with Scapy Part 3 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/27/2023
# Purpose:                      The final iteration of your network scanning tool will perform the following:
#                               
#                               Ping an IP address determined by the user.
#                               If the host exists, scan its ports and determine if any are open.
#                                   In Python, combine the two modes (port and ping) of your network scanner script.
#                                   Eliminate the choice of mode selection.
#                                   Continue to prompt the user for an IP address to target.
#                                   Move port scan to its own function.
#                                   Call the port scan function if the host is responsive to ICMP echo requests.
#                                   Print the output to the screen.



# TCP packet
#Assisted with class video
# Scan User input as host 
def port_scanner(host):
    # User input as integers
    start_port = int(input("Enter start port number: "))
    end_port = int(input("Enter end port number: "))
    # Empty list for ports
    open_ports = []
    # scan each port
    for port in range(start_port, end_port + 1):
        # TCP Packet into response variable
        response = sr1(IP(dst=host) / TCP(sport=port, dport=port, flags="S"), timeout=1, verbose=0)
        # No response
        if response is None:
            print(f"Port {port} is filtered or response is not received.")
        #  TCP response and flag
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # Send RST packet
            send_rst = sr1(IP(dst=host) / TCP(sport=port, dport=port, flags="R"), timeout=1, verbose=0)
            open_ports.append(port)
            print(f"Port {port} is open.")
        # Port closed
        else:
            print(f"Port {port} is closed.")
    # List open ports
    if open_ports:
        print(f"\nOpen ports on {host}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

# ICMP Ping
def ping(host):
    response = sr1(IP(dest=host) / ICMP(), timeout=1, verbose=0)
    # ICMP unresponsive
    if response is None:
        print(f"Host {host} is down or unresponsive.")
        # Host not reachable
        return False
    # Type 3
    elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
        print("Host is blocking traffic.")
        # Host not reachable
        return False
    # Host responding
    else:
        print("Host is responding")
        return True

# Main
def main():
    # User Host IP
    host = input("Enter host IP address: ")
    # If host reachable scan open ports
    if ping(host):
        port_scanner(host)

if __name__ == "__main__":
    main()

# End
# ChatGPT Assisted