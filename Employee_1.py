class Employee_1(object):
    
    #private instance 
    __instance=0
    
    #protected instance that is inherited available to sub class
    _class_info="Inside the Employee class"
    def __init__(self,name=None,loc=None,grade=None,sal=0):
        self.name= name
        self.loc=loc
        self.grade=grade
        type(self).__instance+=1
        
    #worked with protected instance   
    @classmethod
    def whose_instances(cls):
        print("Inside class",cls._class_info)
    
    #below is decorator with@ annotations
    #static method does not take first argument as self instance  
    @staticmethod
    def count_instances():
        return Employee_1.__instance
        
    def __del__(self):
        print("The object instance is destroyed")
        
    def __str__(self):
        return f"Name is {self.name}, Location is {self.loc} and grade is {self.grade}"
    
    def __repr__(self):
        return "Name " +self.name + " Location " + self.loc + " Grade " + self.grade
     
    #Instance method      
    def employee_details(self):
        print("Name = ",self.name)
        print("Grade = ",self.grade)
        print("Loc = ",self.loc)
        
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        return self.name
    
    def set_grade(self,grade):
        self.grade=grade
        
    def get_grade(self):
        return self.grade
    
    def set_location(self,loc):
        self.grade=loc
    
    def get_location(self):
        return self.loc
        
    def salary_details(self):
        if (self.grade=="E1"):
            self.sal=8000
        elif (self.grade=="E2"):
            self.sal=5000
        else:
            print("Grade does not match")
            
class Mnc_Employee(Employee_1):
    _class_info="MNC employee"
    
            
def main():
    print("hello")
    print("Instance count before instance creation is ",Employee_1.count_instances())
    emp1 = Employee_1("Shree","Germany","E1")
    mnc1 = Mnc_Employee()
    Employee_1.whose_instances()
    Mnc_Employee.whose_instances()
    print(type(emp1))
    print(emp1,type(emp1))
    print("Instance count after instance creation is ",Employee_1.count_instances())
    
    # emp2 = Employee_1("Sneha","UK","E2")
    # emp3 = Employee_1()
    # emp1.employee_details()
    # emp1.salary_details()
    # print(f"emp1.name salary is ",emp1.sal)
    # print("*"*50)
    # emp2.employee_details()
    # emp2.salary_details()
    # print(f"emp2.name salary is ",emp2.sal)
    # emp3.employee_details()
    # emp3.salary_details()
    # print(f"emp3.name salary is ",getattr(emp3, 'sal',0))
    
    # print("Instance attributes are stored in form of dictionaries")
    # print(emp1.__dict__)
    # print(emp2.__dict__)
    # print(emp3.__dict__)
    
    #Sprint(Employee_1.__dict__)
 
 
if __name__=="__main__":
     main()
 
 
        