'''Rectangle Area & Perimeter
Create a class Rectangle with:
Attributes: length, width.
Method area() → return area.
Method perimeter() → return perimeter.'''

#Creating Class
class Rectangle:
    def __init__(self,length,width): #constructor
        self.length=length
        self.width=width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        x=2 * (self.length + self.width)
        return x
    
#main body
value1=Rectangle(10,2)
value2=Rectangle(5,3)
x1=value1.area()
x2=value2.area()
x3=value1.perimeter()
x4=value2.perimeter()
print("Area of value1",x1)
print("perimeter of value1",x3)

print("Area of value2",x2)
print("perimeter of value2",x4)
