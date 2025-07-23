'''Write a python program to create a class named Shape. In Shape class create a
method named setValue(), this method initialize side of shape. By inheriting Shape
class create a new class Square. In Square class create a method area(), this method
return area of square. Now by inheriting Shape class create a new class Cube. In
Cube class create a method volume(), this method return volume of cube. Now Test
Square and Cube classes.
'''

class Shape:
    def setValue(self, side):
        self.side = side

class Square(Shape):
    def area(self):
        return self.side ** 2

class Cube(Shape):
    def volume(self):
        return self.side ** 3

s = int(input("Enter the side: "))

sq = Square()
sq.setValue(s)
cu = Cube()
cu.setValue(s)

print("Area of Square:", sq.area())
print("Volume of Cube:", cu.volume())