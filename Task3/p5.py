# Write a python program to create a function named rev(), in rev() function pass a
# string and this function return reverse string

def rev(string):
    rever=string[ : : -1]
    return rever
string=input("Enter the string:")
result=rev(string)
print("Reverse string is:",result)
