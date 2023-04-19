class Animal():
    def __init__(self,name="",type=""):
        self.name=name
        self.type=type
        print("Object has been created successfully")
    
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        return self.name

    def set_type(self,type):
        self.type=type
        
    def get_type(self):
        return self.type
    
    def __del__(self):
        print("Object is destroyed")
        
    def __str__(self):
        return f"Animal name {self.name} Animal Type {self.type}"
        
if __name__=="__main__":
    horse=Animal()
    horse.set_name("popeye")
    horse.set_type("land Animal")
    print("Horse name ", horse.get_name())
    print(horse)
    print("*"*50)
    penguin=Animal()
    penguin.set_name("jello")
    penguin.set_type("sea Animal")
    print("Penguin name ", penguin.get_name())
    print(penguin)
    
    print(horse.__dict__)
    print(penguin.__dict__)
    print(Animal.__dict__)
    
    
    
        
    
        
        