# Write a python program to create a set of ten numbers by taking input from user.
# Now traverse set elements.

a=set()
num=int(input("Enter the range:"))
for i in range(1,num+1):
    s=int(input())
    a.add(s)
print("Set:",a)
print("Traversing set elements:")
for elm in a:
    print(elm)