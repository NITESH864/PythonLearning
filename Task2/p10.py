# Write a python program to reverse the digits of given number.
num=int(input("Enter the number:"))
n=num
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)