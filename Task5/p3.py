'''Write a python program to create a class with name ‘Rectangle’. In ‘Rectangle’ class
take two instance variables length and breadth. Now create a parameterized
constructor to initialize variables and create a method area() which return area of
rectangle. Test the class ‘Rectangle’.'''

class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
	def area(self):
		return self.length*self.breadth

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))

test=Rectangle(l,b)	

print("Area of rectangle:",test.area())
