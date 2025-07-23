'''Write a python program to take coordinates of a point as input and determine its quadrant.'''

x=float(input("Enter the x-coordinates : "))
y=float(input("Enter the y-coordinates : "))

if(x>0 and y>0):
	point="Quadrent I"
elif(x<0 and y>0):
	point="Quadrent II"
elif(x<0 and y<0):
	point="Quadrent III"
elif(x>0 and y<0):
	point="Quadrent IV"
elif(x==0 and y!=0):
	point="on the y axis"
elif(x!=0 and y==0):
	point="on the x axis"

else:
	point="On the Origin"


print(x,",",y ,"the point are in the ",point)


