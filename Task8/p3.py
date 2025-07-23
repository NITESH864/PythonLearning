#Write a program in python to search a substring in given string

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to search: ")

if sub_str in main_str:
    print("Substring found!")
else:
    print("Substring not found.")