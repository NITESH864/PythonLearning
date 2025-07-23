'''Write a program in python to take a decimal number as input and convert it into
binary, octal and hexa-decimal equivalent'''

num = int(input("Enter a decimal number: "))

print("Binary equivalent:", bin(num))
print("Octal equivalent:", oct(num))
print("Hexadecimal equivalent:", hex(num))