'''Write a program in python to open a file for read operation. Also handle
FileNotFoundError'''

filename = input("Enter the filename to open: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")