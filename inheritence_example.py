class Rectangle:
    
    def __init__(self,length,breadth):
	    self.length=length
	    self.breadth=breadth
     
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.breadth+self.length)

        
class Square(Rectangle):
    def __init__(self,length):
        self.length=length
        #super().__init__(length,length)
        #or
        super(Square,self).__init__(length,length)
    def are_wild(self):
        print("They love to eat every other creature ...Definitely Scary!!!")
        
sample_shark=Square(4)
#call to parent function
print("Area is {}".format(sample_shark.area()))
#call to overidden function in child class
sample_shark.are_wild()
    
    