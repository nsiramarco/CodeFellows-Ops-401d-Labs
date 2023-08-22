#!/usr/bin/python3
import os


# Script Name:                  Signature-based Malware Detection Part 1 of 3
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      08/21/2023
# Purpose:                      In Python, write a script that will:
#                               
#                               Prompt the user to type in a file name to search for.
#                               Prompt the user for a directory to search in.
#                               Search each file in the directory by name.
#                               TIP: You may need to perform different commands depending on what OS you’re executing the script on.
#                               
#                               For each positive detection, print to the screen the file name and location.
#                               At the end of the search process, print to the screen how many files were searched and how many hits were found.
#                               The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
#                               



def search_files(directory, filename):
    hits = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            hits.append(os.path.join(root, filename))
    return hits

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

# Resources

#       How to Find Files and Folders in Linux Using the Command Line - https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
#       How to Use Find from the Windows Command Prompt - https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/