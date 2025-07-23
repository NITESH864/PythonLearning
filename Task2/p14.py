''' Write a python program to print Fibonacci series up to n terms, where value of n is
entered by user'''

num=int(input("Enter the number of terms:"))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(3,num+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

         
