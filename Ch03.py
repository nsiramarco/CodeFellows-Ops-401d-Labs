#!/usr/bin/env python3
import os
import smtpd
import smtplib, time, datetime
from getpass import getpass


# Script Name:                  Uptime Sensor Tool Part 2 of 2
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/12/2023
# Purpose:                      In Python, add the below features to your uptime sensor tool.
#                               
#                               The script must:
#                               
#                               Ask the user for an email address and password to use for sending notifications.
#                               Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
#                               Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
#                               Important Notes
#                               
#                               DO NOT commit your email password in plain text within your script to GitHub as this easily becomes public.
#                               Create a new “burner” account for this exercise. Do not use an existing email account.


# Variables

up = "The Ip address host is up!"
down = "The Ip address host is down!"

email = input("Enter Email: ")
password = getpass("Enter Password: ")
ip = input("Enter ip  to monitor")

last = 0
ping_result = 0

# Function alert Up

def Alertup():
    now = datetime.datetime.now()
    #SMTP sessiom
    s = smtplib.SMTP(smtp.gmail.xom, '587')
    #encryption
    s.starttls()
    #Start SMTP session
    s.login(email, password)

    message = "Server is up and running"
    #Send email
    s.sendmail("bot@codefellows.com", email, message)
    #close 
    s.quit()

# Function Alert Down
def Alertdown():
    now = datetime.datetime.now()
    #SMTP sessiom
    s = smtplib.SMTP(smtp.gmail.xom, '587')
    #encryption
    s.starttls()
    #Start SMTP session
    s.login(email, password)

    message = "Server is down"
    #Send email
    s.sendmail("bot@example.com", email, message)
    #close 
    s.quit()

#Function for ping
def ping_test():
    now = datetime.datetime.now()

    global ping_result
    global last
    
    #ping status result
    if ((ping_result != last) and (ping_result == up)):
        #change value 
        last = up
        #send email
        send_Alertup()

    elif((ping_result != last) and (ping_result == down)):
        #change value
        last = down
        #send email
        send_Alertdown()

    # send ping 
    response = os.system("ping -c 1 " + ip)

    # Evaluate ping
    if response == 0:
        ping_result = up
    else:
        ping_result = down
    print(str(now) + ping_result + " to " + ip)


# Main

# While loop
while True:
    ping_test()
    time.sleep(2)


#END