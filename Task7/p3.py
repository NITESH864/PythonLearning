'''Write a program in python to find division of two numbers. Also handle ValueError
and ZeroDivisionError in same program.'''

a=eval(input("Enter the first number:"))
b=eval(input("Enter the second number:"))

try:
    if b==0:
        print("Error, Division of zero is not allowed")

    else:
        print("Division of two number:",a/b)
except ValueError:
    print("Invalid input") 
