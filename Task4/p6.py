# Write a python program to find number of occurrences of each vowel present in the
# given string?
count=0
str=input("Enter the string:")
vol='aeiouAEIOU'
for char in str:
    if char in vol:
        count=count+1
print("Char is present:",count)
