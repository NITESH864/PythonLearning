#Write a program in python to take full name as input. Now display short name of user

full_name = input("Enter your full name: ")
names = full_name.strip().split()

if len(names) > 1:
    short_name = ".".join(name[0].upper() for name in names) + "."
    print("Short name:", short_name)
else:
    print("Short name:", full_name[0].upper() + ".")