class Circle():
    _pi= 3.14
    def __init__(self,r):
        self.rad=r
    @property
    def rad(self):
        return self.__rad
    @rad.setter
    def rad(self,val):
        if val<-1:
            self.__rad=1
        elif val>5:
            self.__rad=5
        else:
            self.__rad=val
    def area(self):
        return Circle._pi*self.rad*self.rad



if __name__=='__main__':
    c= Circle(4)
    # c.set_radius(7)
    
    print("Area of Circle ",c.area())
        
        