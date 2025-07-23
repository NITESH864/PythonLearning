'''Write a python program to create a class with name ‘MyClass’. In MyClass create a
function sayHello(). In sayHello() function pass name of user, and display user name
with Hello, message. Test class ‘MyClass’.'''

class MyClass():
	def sayHello(self,name):
		self.name=name
		
	def display(self):
		print("Name of myclass:",self.name)

test=MyClass()
name=input("Enter the name:") 
test.sayHello(name)
test.display()


	
	