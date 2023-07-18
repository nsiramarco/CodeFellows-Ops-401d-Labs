#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet



# Script Name:                  File Encryption Script Part 1 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/18/2023
# Purpose:                      In Python, create a script that utilizes the cryptography library to:
#                               
#                               Prompt the user to select a mode:
#                               Encrypt a file (mode 1)
#                               Decrypt a file (mode 2)
#                               Encrypt a message (mode 3)
#                               Decrypt a message (mode 4)
#                               If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#                               If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#                               Depending on the selection, perform one of the below functions. You’ll need to create four functions:
#                               
#                               Encrypt the target file if in mode 1.
#                               Delete the existing target file and replace it entirely with the encrypted version.
#                               Decrypt the target file if in mode 2.
#                               Delete the encrypted target file and replace it entirely with the decrypted version.
#                               Encrypt the string if in mode 3.
#                               Print the ciphertext to the screen.
#                               Decrypt the string if in mode 4.
#                               Print the cleartext to the screen.
                           

# Declaration of functions
# Create key
def generate_key():
    return Fernet.generate_key()
# Add the key
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()
# Save the key
def save_key(key_file, key):
    with open(key_file, 'wb') as file:
        file.write(key)
# Encrypt data
def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
# Decrypt Data
def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
# Encrypt the message
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    print("Encrypted message:", encrypted_message.decode())
# Decrypt the message
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted message:", decrypted_message.decode())

# Main
# Find if key file already exists
def main():
    key_file = 'encryption_key.key'
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key_file, key)
    # Create if it does not exist
    else:
        key = load_key(key_file)

# Display a menu
    print("Select a mode:")
    print("1 - Encrypt file")
    print("2 - Decrypt file")
    print("3 - Encrypt message")
    print("4 - Decrypt message")
# User inserts mode
    mode = int(input("Enter mode number: "))
    # Mode Selection/Call function 
    if mode == 1:
        encrypt_file(key, input("Enter filepath of the file to encrypt: "), input("Enter filepath to save the encrypted file: "))
        print("File encrypted successfully.")

    elif mode == 2:
        decrypt_file(key, input("Enter filepath of the file to decrypt: "), input("Enter filepath to save the decrypted file: "))
        print("File decrypted successfully.")

    elif mode == 3:
        encrypt_message(key, input("Enter cyphertext message to encrypt: "))

    elif mode == 4:
        decrypt_message(key, input("Enter ciphertext message to decrypt: "))
# If user enters something else display error message
    else:
        print("Invalid mode selection.")

if __name__ == "__main__":
    main()

# END