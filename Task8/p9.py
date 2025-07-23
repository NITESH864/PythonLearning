# Write a program in python to count digits in an alphanumeric string. 

s = input("Enter an alphanumeric string: ")
count = sum(1 for char in s if char.isdigit())
print("Number of digits in the string:", count)