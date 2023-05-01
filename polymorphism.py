class Animal:
    def __init__(self,name=None):
        self.name=name
        print(f"It's of type",type(self))
    def speak(self):
        raise NotImplementedError("Subclass has to implemented this function")
    
    
class Dog(Animal):
    def __init__(self,name):
       self.name=name
       Animal.__init__(self)
    def speak(self):
        print (f"I am a Dog and i Woof!!!")
    
class Cat(Animal):
    def __init__(self,name):
           self.name=name
           Animal.__init__(self)
    def speak(self):
        print (f"I am a Cat and i Meow!!!")
        
if __name__=="__main__":
    c = Cat("Babloo")
    d = Dog("Mola")
    l=[c,d]
    for i in l:
        i.speak()