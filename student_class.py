'''
Create a class Student that:

Takes name and age as input when creating the object.

Has a method display() that prints'''


#Creating a Class
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name,",","Age:",self.age)

#main body
st1=Student("Preeti",19)
st2=Student("Priya",20)
st1.display()
st2.display()
