# Write a python program to check given number is prime or not.

num=int(input("Enter the number to check:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("number is not prime")
            break
    else:
        print("prime Number")  

else:
    print("Number is not prime")  

