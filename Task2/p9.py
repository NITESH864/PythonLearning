# Write a python program to find sum of digits of given number.
sum=0
num=int(input("Enter the number:"))
n=num
while(n>0):
    mod=n%10
    sum=sum+mod
    n=n//10
print(sum)
