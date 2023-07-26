#!/usr/bin/env python3
import os
from scapy.all import srl, IP, ICMP, TCP

# Script Name:                  
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/25/2023
# Purpose:                      Add the following features to your Network Security Tool:
#                               
#                               User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
#                               ICMP Ping Sweep tool
#                               Prompt user for network address including CIDR block, for example “10.10.0.0/24”
#                               Careful not to populate the host bits!
#                               
#                               Create a list of all addresses in the given network
#                               Ping all addresses on the given network except for network address and broadcast address
#                               If no response, inform the user that the host is down or unresponsive.
#                               If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
#                               Otherwise, inform the user that the host is responding.
#                               Count how many hosts are online and inform the user.


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
        elif (response.getlayer(TCP).flags == None):
            # Notify it's closed (filtered and silently dropped)
            print(f"{host}:{port_dest} is filtered and silently dropped")

else:
      print("Host in unresponsive.")

################ Pending ##################
# Main
def main():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner mode")
    print("2. ICMP Ping Sweep mode")
    choice = int(input("Enter your choice 1 or 2: "))

    if choice == 1:
        # TCP Port Range Scanner mode
        host = "scanme.nmap.org"
        port_dest = 22
        port_scan = 22

        response = srl(IP(dst=host)/TCP(sport=port_scan, dport=port_dest, flags="S"), timeout=1, verbose=0)

        if response and response[0][TCP].flags == 0x12:
            send_rst = srl(IP(dst=host)/TCP(sport=port_scan, dport=port_dest, flags="R"), timeout=1, verbose=0)
            print(f"{host}:{port_dest} is open.")
        else:
            print(f"{host}:{port_dest} is closed or unresponsive.")

    elif choice == 2:
        # ICMP Ping Sweep mode
        network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)

    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()

# End

#                      Resources
#                      [Generating a Range of IP Addresses from a CIDR Address in Python](http://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/)