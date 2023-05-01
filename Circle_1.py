class Circle_1():
    'class attribute'
    pi =3.14
    def __init__(self,radius=1,color=None):
        self.radius=radius
        self.color=color
        self.area=Circle_1.pi*radius*radius
    
    def get_circumference(self):
        return self.radius*2*Circle_1.pi
    
class ChildCircle(Circle_1):
    
    def __init__(self):
        Circle_1.__init__(self,5,"RED")
        print("Within subclass of Circle")
        
    
if __name__=="__main__":
        c= Circle_1(8)
        print("ARea is ",c.area)
        print(f"The circumference is ",c.get_circumference())
        d=ChildCircle()
        print(d.color)
        print(d.get_circumference())
        print(d.area)
        