'''Write a python program to create a class with name ‘Employee’. In Employee class
take three instance variables empid, empname and salary. Create two methods in
Employee class first setEmployee() and second display(). setEmployee() method
initialize instance variables empid, empname, salary and display() method display
value of empid, empname and salary. Now test Employee class.'''

class Employee:
	def setEmployee(self,empid,empname,salary):
		self.empid=empid
		self.empname=empname
		self.salary=salary
		
	def display(self):
		print("the empid:",self.empid)
		print("the empname:",self.empname)
		print("the salary:",self.salary)

empid=input("Enter the id:")
empname=input("Enter the name:")
salary=int(input("Enter the emp salary:"))
print("--------------------------------------------")
e=Employee()
e.setEmployee(empid,empname,salary)
e.display()