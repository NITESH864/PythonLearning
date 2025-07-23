# Write a python program to create a list of five students by taking input from user.
# Now display name of students in ascending and descending order.

lst=[]
for i in range(5):
    name=input("Enter the students name:")
    lst.append(name)
print("Original list",lst)
print("Assending order of name:",sorted(lst))
print("Descending order of name:",sorted(lst,reverse=True))
    
