'''Write a python program to create a class with name ‘Student’. In Student class take
three instance variables rollno, name and fee. Now create a parameterized
constructor to initialize variables and create a method display() which display values
of instance variables. Test the class ‘Student’.'''


class Student:
	def __init__(self,rollno,name,fee):
		self.rollno=rollno
		self.name=name
		self.fee=fee

	def Display(self):
		print("Rollno of student:",self.rollno)
		print("Name of student:",self.name)
		print("Fee of student:",self.fee)

r=int(input("Enter the student rollno:"))
n=str(input("Enter the student name:"))
f=int(input("Enter the student fee:"))
print("-------------------------------------------------")

s=Student(r,n,f)

s.Display()









