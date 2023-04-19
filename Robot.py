class Robot:
    def __init__(self, name=None, build_year=None):
        self.__name = name
        self.__build_year = build_year
    def __repr__(self):
        return "Robot(\"" + self.__name + "\"," +  str(self.__build_year) +  ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
    def set_name(self,name):
        self.__name=name
    def set_build_year(self,build_year):
        self.__build_year=build_year
    def get_name(self):
            return self.__name
    def get_build_year(self):
        return str(self.__build_year)
    def __del__(self):
        print(self.__str__() +" Object is destroyed")
    
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    print(x)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new:", type(new))
    y = Robot()
    y.set_name("Maruti Zen")
    y.set_build_year(2000)
    print("Car Name "+y.get_name()+" Build Year"+y.get_build_year())
    print(y)
    
