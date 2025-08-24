#parent class
class shape:
    length=0
    width=0
    #constructor
    def __init__(self,l,w):
        self.length=l
        self.width=w
    
    #Method 
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
#child class
class box(shape):
    height=0
    
    #constructor
    def __init__(self,l,w,h):
        shape.__init__(self,l,w)
        self.height=h 
        
    #Method
    def volume(self):
        return self.height * self.width * self.length
    
    #Method overriding
    def perimeter(self):
        return 4 * (self.length + self.width + self.height)

#main body
x=box(10,2,4)
y=shape(10,2)
print("Shape class",y.perimeter())
print("Box class",x.perimeter())
print("Box class",x.volume())
