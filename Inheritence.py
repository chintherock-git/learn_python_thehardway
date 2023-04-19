import random
class Robot():
    def __init__(self,name):
        self.name=name
        #random function assih=gns any value which is n>=0.0 and n<=1.0
        self.healthlevel=random.random()
        
    def hello(self):
        print(f"Hello i am Robo {self.name}")
        print(f"I have a health level of {self.healthlevel}")
        
    #overloading method
    def number(self,n,m=None):
        if m:
            return n+m
        else:
            return n
        
    def overloading(self,*args):
        if len(args)==1:
            return args[0]
        elif len(args)>1:
            return list(map(lambda n:n**2,args))
            
        
    def check_help(self):
        if self.healthlevel<0.8:
            print("I need health help")
        else:
            print("I am perfectly healthy")

class My_Robot(Robot):
    #overidden method
    def hello(self):
        #calling parent class method with super() else 
        #super().hello()
        Robot.hello(self)
        self.healthlevel=random.uniform(self.healthlevel,1)
        print(f"My new health level is {self.healthlevel}")
        
if __name__=="__main__":
    r=Robot("Bheem")
    print(r.number(9))
    print(r.number(6,90))
    print(Robot.overloading(r,9,8,4,6,7,9,2))
    # r.hello()
    # r.check_help()
    y=My_Robot("Chinzaa")
    print(type(r))
    print(type(y))
    #isinstance returns True if we compare an object either with the class it belongs 
    # to or with the superclass. Whereas the equality operator only returns True, 
    # if we compare an object with its own class.
    print(isinstance(y,Robot))
    print(isinstance(r,My_Robot))
    # y.hello()
    # y.check_help()
    # Robot.check_help(r)