# Write a python program to create a list of ten numbers by taking input from user.
# Now check a number is presented in list or not.

lst=[]
num=int(input("Enter the Range:"))
for i in range(1,num+1):
    s=int(input())
    lst.append(i)
print(lst)    
check=int(input("Ckeck the number is present or not:"))
if check in lst:
    print("Number is present")
else:
    print("Not Present")    