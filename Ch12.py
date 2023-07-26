#!/usr/bin/python3
import ipaddress
from scapy.all import IP, ICMP, TCP, sr1

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
network="10.10.0.0/24"
ip_list = ipaddress.IPv4Network(network)
host_count = 0

# TCP packet
def port_scanner():
    host = input("Enter the target host IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    open_ports = []

    for port in range(start_port, end_port + 1):
        # TCP Packet into the response variable
        response = sr1(IP(dst=host) / TCP(sport=port, dport=port, flags="S"), timeout=1, verbose=0)

        if response is None:
            print(f"Port {port} is filtered or no response received.")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # Send RST packet
            send_rst = sr1(IP(dst=host) / TCP(sport=port, dport=port, flags="R"), timeout=1, verbose=0)
            open_ports.append(port)
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")

    if open_ports:
        print(f"\nOpen ports on {host}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

# ICMP Ping Sweep
def ping_sweep():
      # CIDR Block
      # Generate IP list
      global ip_list
      global host_count
     
      # ICMP request each host
      for host in ip_list:
        # Exception network address and broadcast
        if host in (ip_list.network_address, ip_list.broadcast_address):
             #Skip first and last
             continue
        # ICMP Pacekt into repsonse variable
        response = sr1(IP(dest=str(host))/ICMP(), timeout=1, verbose=0)
        
        if response is None:
            print(f"Host {host} is down or unresponsive.")

        elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
             print("Host is blocking traffic.")
        
        else:
             print("Host is responding")
             host_count += 1
      
      print(f"Total hosts online: {host_count}")



# Main
#ChatGPT Assisted
def main():
    user_choice = int(input("Choose an option:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\n"))

    if user_choice == 1:
         port_scanner()

    elif user_choice == 2:
        global ip_list
        ip_list = ipaddress.IPv4Network(input("Enter network address including CIDR block (e.g., 192.168.0.0/24): "))
        host_count = 0
        ping_sweep()

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()


   
# End

#                      Resources
#                      [Generating a Range of IP Addresses from a CIDR Address in Python](http://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/)