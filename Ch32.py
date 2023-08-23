#!/usr/bin/python3
import os
import hashlib
import time
import subprocess


# Script Name:                  Signature-based Malware Detection Part 2 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/22/2023
# Purpose:                      Continue developing your Python malware detection tool.
#                               
#                               Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
#                               For each file scanned within the scope of your search directory:
#                               Generate the file’s MD5 hash using Hashlib.
#                               Assign the MD5 hash to a variable.
#                               Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
#                               TIP: You may need to bring in additional Python modules to complete today’s objective.
#                               
#                               The script should be tested to execute successfully in Python3.
#                               



# Function
# Function to generate MD5 hash
def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def search_files(directory, filename):
    hits = []
    for root, _, files in os.walk(directory):
        for file in files:
            if filename in file:
                file_path = os.path.join(root, file)
                md5_hash = generate_md5(file_path)
                file_size = os.path.getsize(file_path)
                hits.append((file_path, md5_hash, file_size))
    return hits

# Main
def main():
    # User input file name to search for
    filename = input("Enter the file name to search for: ")
    # User for directory to search in
    directory = input("Enter the directory to search in: ")

    if os.path.exists(directory):
        # Search each file in the directory by name.
        hits = search_files(directory, filename)
        if hits:
            # For each result found print to the screen the file name, location, MD5 hash, file size, and timestamp.
            print("\nFiles found:")
            for hit in hits:
                file_path, md5_hash, file_size = hit
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"Timestamp: {timestamp}")
                print(f"File Name: {filename}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {md5_hash}\n")
            
            # Quantity of files searched and how many hits were found.
            print("Total files searched:", len(hits))
            print("Total hits found:", len(hits))
        else:
            print("\nNo files found matching the specified name.")
    else:
        print("\nThe specified directory does not exist.")

if __name__ == "__main__":
    main()


# END
# classroom video and chatgpt assisted

# Resources
#           Hashlib Official Documentation - https://docs.python.org/3/library/hashlib.html
#           Python Program to Find Hash of File - https://www.programiz.com/python-programming/examples/hash-file