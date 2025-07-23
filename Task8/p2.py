'''Write a program in python to take a string as input. Now check given string is
palindrome or not'''

s = input("Enter the string: ")

if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")