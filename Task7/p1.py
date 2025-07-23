'''Write a program in python to create a class with name Figure. In Figure class create a
single method named area(), by using area() method find area of square and
rectangle as an example of method overloading.'''

class Figure:
    def area(self,a=None,b=None):
        if a is not None and b is None:
            print("Area of Square:",a**2)
        elif a is not None and b is not None:
            print("Area of Rectangle:",a*b)
c=Figure()
c.area(2)
c.area(3,2)


