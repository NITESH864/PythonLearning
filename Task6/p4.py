'''In program (3) create a class Loan before the code of Payslip class. In Loan class
create a method setLoan() which is used to initialize amt variable. Now inherit Loan
class in Payslip class and in netSalary() method also print salary on hand as
(bs+hra+da-amt). This is an example of hybrid inheritance.'''

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
class Loan:
	def setLoan(self,amount):
		self.amount=amount

class Payslip(Payroll,Loan):
	def netSalary(self,):
		totalSalary=self.bs+self.hra+self.da
		print("Total salary of Employee:",totalSalary)
		salary_on_hand=totalSalary-self.amount
		print("Salary on hand after the loan deduction:",salary_on_hand)
	
pa=Payslip()

id=str(input("Enter the employee id:"))
name=str(input("Enter the employee name:"))
pa.setEmployee(id,name)
print("_______________________")
pa.getEmployee()

bs=float(input("Enter the employee bs:"))
hra=float(input("Enter the employee hra:"))
da=float(input("Enter the employee da:"))
pa.setPayroll(bs,hra,da)
print("_______________________")
pa.getPayroll()

amount=float(input("Enter the loan amount:"))
pa.setLoan(amount)
print("_______________________")
pa.netSalary()


