#!/usr/bin/env python3
import os
import ping3
import time
import datetime

# Script Name:                  Uptime Sensor Tool
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/11/2023
# Purpose:                      In Python, create an uptime sensor tool that uses ICMP packets to evaluate
#                               if hosts on the LAN are up or down.
#                               
#                               The script must:
#                               
#                               - Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#                               - Evaluate the response as either success or failure.
#                               - Assign success or failure to a status variable.
#                               - For every ICMP transmission attempted, print the status variable along with
#                                 a comprehensive timestamp and destination IP tested.
#                               - Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

#Function
#Single ICMP Packet to Specific IP Address
def Single_ICMP():
    icmp_packet = '8.8.8.8'
    while True:

        # Timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # response true=Up or false=Down
        response_status = 'Up' if ping3.ping(icmp_packet) else 'Down'

        # Print variable, timpestamp and destination ip tested
        print(f'[{timestamp}] Destination: {icmp_packet} | Status: {response_status}')
        
        # Request ping every two seconds
        time.sleep(2)
# Execute conditional statement
if __name__ == '__main__':
    Single_ICMP()
  
# End