#!/usr/bin/python3
import getpass 
import sys
import time

# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/31/2023
# Purpose:                      In Python, create a script that prompts the user to select one of the following modes:
#                               
#                               Mode 1: Offensive; Dictionary Iterator
#                               Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#                               Add a delay between words.
#                               Print to the screen the value of the variable.
#                               
#                               Mode 2: Defensive; Password Recognized
#                               Accepts a user input string.
#                               Accepts a user input word list file path.
#                               Search the word list for the user input string.
#                               Print to the screen whether the string appeared in the word list.


# Functions
# First Mode: iterates through wordlist
def iterator():
    # user input complete filepath
    filepath = input("Enter filepath for woordlist")
    # Open wordlist
    file  = open(filepath, 'r')
    # Read file first line on wordlist/ variable called line
    line  =  file.readline()

    #while loop for each line in wordlist
    while line:
        # not reading empty trailing space
        line = line.rstrip()
        #line variable into word
        word = line
        print(word)
        time.sleep(1)

        # get next line in wordlist
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

    # Check if the input string is in the word list
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
if (mode == '1'):
    iterator()
elif (mode == '2'):
    password_recognized()
elif (mode == '3'):
    sys.exit()
else:
    print("Invalid mode selection, Please choose 1, 2 or 3. ")

# END
# Assited with class video and chatGPT reviewed for errors

    #Resources
#       [Iterate over a set in Python](https://www.geeksforgeeks.org/iterate-over-a-set-in-python/)
#       [RockYou Password List (download, and unzip)](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)
