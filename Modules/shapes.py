from math import pi
class circle():
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return pi * self.radius **2
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
