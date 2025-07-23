# Write a python program to create a list of ten numbers by taking input from user
# named AR. Now copy even numbers in list EAR and odd numbers in list OAR. Now
# display elements of EAR and OAR.

AR=[]
num=int(input("Enter the number:"))
for i in range(1,num+1):
    s=int(input())
    AR.append(s)
print(AR)    
EAR=[]
OAR=[]
for i in AR:
    if i%2==0:
        EAR.append(i)
    else:
        OAR.append(i)    
print("Even number are:",EAR)
print("Odd number are:",OAR)