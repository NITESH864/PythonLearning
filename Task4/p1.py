# Write a python program to create a list of ten numbers by taking input from user.
# Now find sum and average of numbers.

lst=[]
sum=0
num=int(input("Enter the range:"))
for i in range(num):
    a=int(input())
    lst.append(a)
    sum=sum+a
print(lst)     
print("Sum of numbers:",sum)
print("Average of numbers:",sum/num)
    