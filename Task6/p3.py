'''Write a python program to create a class Employee. In Employee class take two
instance variables empid and empname. In Employee class create two methods
setEmployee() and getEmployee(). setEmployee() method is used to initialize
instance variables empid and empname whereas getEmployee() method is used to
display values of empid and empname. By inheriting Employee class create a new
class Payroll. In Payroll class create three instance variables bs, hra and da. In Payroll
class create two methods setPayroll() and getPayroll(). setPayroll() method is used to
initialize variables bs, hra and da whereas getPayroll() method is used to display
values of bs, hra and da. Now by inheriting Payroll class create a new class Payslip. In
Payslip class create a method named netSalary() which displays net salary with
addition of basic salary, hra and da. Now test Payslip class. This is an example of
multilevel inheritance.'''

class Employee:
	def setEmployee(self,empid,empname):
		self.empid=empid
		self.empname=empname
	def getEmployee(self):
		print("Employee id is:",self.empid)
		print("Employee name:",self.empname)

class Payroll(Employee):
	def setPayroll(self,bs,hra,da):
		self.bs=bs
		self.hra=hra
		self.da=da
	def getPayroll(self):
		print("Basic salary of employee:",self.bs)
		print("House Rent Allowance of employee:",self.hra)
		print("Dearness Allowance of employee:",self.da)

class Payslip(Payroll):
	def netSalary(self,):
		totalSalary=self.bs+self.hra+self.da
		print("Total salary of Employee:",totalSalary)
	
pa=Payslip()

id=str(input("Enter the employee id:"))
name=str(input("Enter the employee name:"))
pa.setEmployee(id,name)
print("_______________________")
pa.getEmployee()

bs=str(input("Enter the employee bs:"))
hra=str(input("Enter the employee hra:"))
da=str(input("Enter the employee da:"))
pa.setPayroll(id,hra,da)
print("_______________________")
pa.getPayroll()
print("_______________________")
pa.netSalary()

