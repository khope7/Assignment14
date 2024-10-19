#Task 1: Directory Inspector:
#
#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.
#
#Code Example:
#    import os
#
#    def list_directory_contents(path):
#        # List and print all files and subdirectories in the given path

#Instantiating list_directory_contents function
import os

#Creating function to create folder, file, and to move file into folder and print directory contents
def list_directory_contents(path):
#Created try and except blocks to catch for errors while creating writing moving and listing files and folders
    try:
#Created folder for directory contents to show
        os.makedirs('DirectoryInspector', exist_ok = True)
#Used with as function to create a new file if one doesnt exist and write within
        with open('DirectoryInspector.txt', 'w') as file:
            file.write("Additional file created for Direcory Inspector Task")
#Moving newly created file into newly created folder
        old_path = 'DirectoryInspector.txt'
        new_path = os.path.join('DirectoryInspector', 'DirectoryInspector.txt')
        os.rename(old_path, new_path)
        print(f"Moved {old_path} to {new_path}")
#Calling directory from directory function and printing
        files = os.listdir(path)
        print(f"\nHere are the current folders and files:\n{files}")
#Creating user friendly interface for exiting program
        print("\nThank you, exiting")
#Created to catch for permission errors
    except PermissionError:
        print("You dont have permission to write to this file")
#Created to catch for errors occured while writing
    except IOError:
        print("An issue occurred while writing to the file")
#Created to catch for file not existing
    except FileNotFoundError:
        print("The file doesnt exist!")
#Created for all other possible errors
    except Exception as e:
        print(f"A general error occurred: {e}")

#Created directory function to find current directory and pass to list_directory_contents function
def directory():
    current_directory = os.getcwd()
    print("Creating Directory Inspector folder, then creating Directory Inspector file and printing:")
    list_directory_contents(current_directory)

#Calling directory to run
directory()