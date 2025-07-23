#Write a python program to demonstrate super keyword.

class Parent:
	def __init__(self):
		print("Parent constructor is called")

	def hello(self):
		print("This class is from Parent")

class Child(Parent):
	def __init__(self):
		print("Child constructor is called")
		super().__init__()

	def hello(self):
		super().hello()
		print("This class is from Child")
			
c=Child()
c.hello()