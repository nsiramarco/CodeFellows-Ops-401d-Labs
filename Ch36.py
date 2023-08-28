#!/usr/bin/python3
import os, time, sys
import socket

# Script Name:                  Web Application Fingerprinting
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/28/2023
# Purpose:                      In Python create a script that executes from a Linux box to perform the following:
#                               
#                               Prompts the user to type a URL or IP address.
#                               Prompts the user to type a port number.
#                               Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
#                               Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
#                               Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
#                               NOTE: Be sure to only target approved URLs like scanme.nmap.org or web servers you own.


# Functions
def netcat_scan(target, port):
    try:
        # Create TCP Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the target IP and port
        s.connect((target, int(port)))
        # Receive up to 1024 bytes of data and decode
        banner = s.recv(1024).decode()
        # Print banner info
        print("Netcat banner:", banner)
        # Close Socket
        s.close()
    except Exception as e:
        print("Netcat banner grabbing failed:", str(e))


def telnet_scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        banner = s.recv(1024).decode()
        print("Telnet banner:", banner)
        s.close()
    except Exception as e:
        print("Telnet banner grabbing failed:", str(e))

def nmap_scan(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Using MySQL port for Nmap banner grabbing
        s.connect((target, 3306))  
        banner = s.recv(1024).decode()
        print("Nmap banner:", banner)
        s.close()
    except Exception as e:
        print("Nmap banner grabbing failed:", str(e))


# Main
# Menu Output
def main():
    while True:
        print("Banner Scanning Menu:")
        print("1. Netcat")
        print("2. Telnet")
        print("3. Nmap")

        choice = input("Enter your choice 1-3: ")

        if choice not in ('1', '2', '3'):
            print("Invalid choice. Please enter 1, 2, or 3.")
              # Restart the loop until valid choice selected
            continue

        target = input("Enter the URL or IP address: ")
        port = input("Enter the port number: ")

        if choice == '1':
            netcat_scan(target, port)
        elif choice == '2':
            telnet_scan(target, port)
        elif choice == '3':
            nmap_scan(target)

        break  # Exit the loop after successful banner grabbing


# Run Function execution
if __name__ == "__main__":
    main()




# END

# Resources
#           Multiple Ways to Banner Grabbing - https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/