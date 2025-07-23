# Write a python program to create a function named substr(), in substr() function
# pass a string and substring. If substring is presented in string then return true or
# return false.

def substr(string,substring):
    if substring in string:
        return True
    else:
        return False
    
string=input("Enter the string:")
substring=input("Enter the substring:")

s=substr(string,substring)
print("Substring is present in the string=",s)