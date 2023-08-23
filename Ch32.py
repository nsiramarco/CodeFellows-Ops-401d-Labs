#!/usr/bin/python3
import os
import subprocess


# Script Name:                  Signature-based Malware Detection Part 1 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/21/2023
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
def search_files(directory, filename):
    hits = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            hits.append(os.path.join(root, filename))
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
            # For each result found print to the screen the file name and location.
            print("\nFiles found:")
            for hit in hits:
                print(hit)
            
            # Quantity of files searched and how many hits were found.
            print("\nTotal files searched:", len(hits))
            print("Total hits found:", len(hits))
        else:
            print("\nNo files found matching the specified name.")
    else:
        print("\nThe specified directory does not exist.")

if __name__ == "__main__":
    main()


# END
# classroom video and chatgpt assisted