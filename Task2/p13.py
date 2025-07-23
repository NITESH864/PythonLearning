'''write a python program to print series of prime numbers in given range. Range
must be created by taking input from user.'''

lower=int(input("Enter the lowere limit :"))
upper=int(input("Enter the upper limit :"))

for num in range(lower,upper+1):
    if num>=2:
        for i in range(2,num):
            if num%i==0:
                break 
        else:
            print(num,end=" ")
     
        
