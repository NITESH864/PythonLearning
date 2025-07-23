'''Write a program in python to create a class with name Bank. In Bank class create a
method interest() which return 0 value. Now override interest method in class Sbi
and Pnb.'''

class Bank:
    def interest(self):
        return 0
class sbi(Bank):
    def interest(self):
        print("This is from class sbi")

class pnb(Bank):
    def interest(self):
        print("This is from class pnb ")

c=Bank()
c.interest()

s=sbi()
s.interest()

p=pnb()
p.interest()
