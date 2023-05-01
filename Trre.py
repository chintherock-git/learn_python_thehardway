class Myclass():
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
    


class Tree():   
    '''This class defines the class Tree and the characteristics of it '''
    def __init__(self,type,age, takes="CO2",gives="O2"):
        self.__type=type
        self._age=age
        self.takes=takes
        self.gives=gives
        
    def __call__(self,isSeasonal):
        if (isSeasonal=="True"):
            season="This is seasonal"
        elif (isSeasonal=="False"):
            season="This is not seasonal"
        self.isSeasonal=season
        
    def setType(self,type):
        self.__type=type
        
    def getType(self):
        return self.__type
        
    def setAge(self,age):
        self._age=age
    
    ##he __repr__ method is used by the eval() function to create a string that can be used to recreate the object later.
    #it has to have exact syntax of the string format when ur creating the instance of the object
    #else it will start to give to Syntax error
    
    def __repr__(self):
        return "Tree("+"\""+self.__type+"\""+","+str(self._age)+")"
        
    def __str__(self):
        return "The Tree type is "+self.__type +" the age is "+str(self._age)
    
       
if __name__=='__main__':
    print(Tree.__doc__)
    x = Tree("Tall tree",3)
    print(f"This print s the instance of Tree when str() and repr() is not defined :",x)
    print(f"prints the memebers and value inside the class instance :",x.__dict__)
    print(x.gives)
    #str is function used to print the for end user
    print("Internally calls the str function ",x)
    x_repr=repr(x)
    print(x_repr,type(x_repr))
    new= eval(repr(x))
    print(type(new))
    y= Tree("Plant", .6)
    print(y("True"))
    print(y.isSeasonal)
    v=Myclass(dict(start=dict(a=1,b=2), end=dict(q=5,z=9) ))
    print(len(v))
    

    