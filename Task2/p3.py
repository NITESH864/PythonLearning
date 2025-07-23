'''
Write a python program to find roots of quadratic equation ax2+bx+c=0.
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
'''
import math
a=float(input("Enter the a : "))
b=float(input("Enter the b : "))
c=float(input("Enter the c : "))

dis=b**2-4*a*c
if dis>0:
    root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("The roots are real and different",root1,root2)
elif dis==0:
    root1=-b/(2*a)
    print("The roots are real and the same",root1)
else:
    root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("The roots are complex",root1,root2)




