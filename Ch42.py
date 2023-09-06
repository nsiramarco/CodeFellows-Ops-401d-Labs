#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) IP Protocol Scan: Range 0-255            \n""")
print("You have selected option: ", resp)

range = '1-50'

# Port range user input
port_range = input("Enter a port range: ")


if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # UDP scan option
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    ### IP Protocol Scan
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sO')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
else:
    print("Invalid option. Please select options 1, 2, or 3 and try again.")
    resp = input("Select scan to execute:\n1) SYN ACK Scan\n2) UDP Scan\n3) IP Protocol Scan\n") 
