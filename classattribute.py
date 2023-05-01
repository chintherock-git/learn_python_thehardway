class A():
    counter=1
    constitutional_laws=("Freedom of press","Equality in India","Right to Privacy",
                         "Freedom of Religion")
    
def __init__(self,name=None):
    self.name=name
    
if __name__=="__main__":
    a=A()
    print(a.__class__.counter)
    
    for number,text in enumerate(A.constitutional_laws):
        print(str(number+1)+": "+text)

class Toy():
    
    #will consists of instance variables and class variables and methods special and instance methods
    toy_brand="Hamleys"
    counter=0
    
    #it gets called when ur creating an instance of class
    #self means the instance that is callingf the method
    def __init__(self,type,category,name=None):
        #public attributes
        self.type=type
        self.category=category
        self.name=name
        Toy.counter+=1
        
    def __del__(self):
        Toy.counter-=1        

        
if __name__=="__main__":
    #creating objects/instance of class or instantiation
    print(Toy.counter)
    first_toy = Toy("soft toy","under 10","push back car")
     # print(first_toy.name and type)
    print(first_toy.name)
    print(first_toy.type)
    print(f"Count of toy after first object is created "+str(Toy.counter))
    print("Accessing class variable with instance "+str(first_toy.counter))
    first_toy.counter=89
    #displays updating class attribute through instance does no effect on the class attribute value 
    print("Accessing via class "+str(Toy.counter))
    print(first_toy.__class__.counter)
    print("*********************************************************")
    #Use of getattr function to avoid exception when attribute is not present for instance 
    print(first_toy.variable)

    
    second_toy=Toy("plastic toy","between 10-12")
    print(second_toy.name)
    print(second_toy.type)
    print(f"Count of toy after 2ND object is created "+str(Toy.counter))
    
    print(first_toy.__dict__)
    print(second_toy.__dict__)
    print("*******class variable/attribute*******")
    print(Toy.toy_brand)
    print(first_toy.toy_brand)
    print(second_toy.toy_brand)
    
    Toy.toy_brand="Barbie"
    print(first_toy.toy_brand)
    print(second_toy.toy_brand)
    
    first_toy.toy_brand="Hot wheels"
    print(first_toy.toy_brand)
    print(second_toy.toy_brand)
    
    print(Toy.toy_brand)
    print(type(first_toy))
    
    del first_toy
    print(Toy.counter)
    del second_toy
    print(Toy.counter)
    
    
    
    
    