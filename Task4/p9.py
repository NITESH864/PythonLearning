# Write a python program to create a dictionary by taking input from user. Now
# traverse elements of dictionary.

dict={}
key_value=int(input("Enter the number of key value you want to print:"))
for i in range(key_value):
    key=input("Enter the key:")
    value=input("Enter the the value:")
    dict[key]=value
print("Dictionary:",dict)

for key,value in dict.items():
    print(key,value)