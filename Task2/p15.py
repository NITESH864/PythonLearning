#Write a python program to check given number is Armstrong or not.

num=int(input("Enter the number:"))
num1=len(str(num))
sum=0
temp=num
while(temp>0):
    digit=temp%10
    cube=digit**num1
    sum=sum+cube
    temp=temp//10

if sum==num:
    print("Armstrong")
else:
    print("Not")


