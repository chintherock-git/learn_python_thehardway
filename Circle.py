import math, unittest
class Circle:
    def __init__(self):
        self.rad = float(input("Enter radius: "))
 
    def area(self):
        return math.pi*self.rad**2
 
    def circum(self):
        return 2*math.pi*self.rad
 
