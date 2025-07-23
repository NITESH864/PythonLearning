# Write a python program to create a function calc(), write code to find summation,
# subtraction, multiplication and division and return result in form of list. Now test
# calc() function.
def calc(a,b):
    s=a+b
    sub=a-b
    m=a*b
    if b!=0:
      d=a/b
    else:
       d="Error"
    return[s,sub,m,d]
 
v=calc(5,0)    
print("Summation",v[0])
print("Subtraction",v[1])
print("Multiplication",v[2])
print("Division",v[3])
