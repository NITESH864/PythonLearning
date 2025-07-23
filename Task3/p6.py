#Write a python program to find factorial of given number using ‘Recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
