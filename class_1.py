class Employee(object):
    def __init__(self,name,loc,sal_grade):
        self.name=name
        self.loc=loc
        self.sal_grade=sal_grade
        
    def __del__(self):
        print("Object is destroyed")
    
    def employee_details(self):
        print(f"Employee Name is {self.name}")
        print(f"Employee Location is {self.loc}")
        print(f"Employee Salary Grade is {self.sal_grade}")
        
def main():
    emp1=Employee("Sheena","Amritsar","E2")
    emp2=Employee("Lohit","Hyderabad","E1")
    emp3=Employee("Sarmistha","Bangalore","E5")
    
    emp1.employee_details()
    emp2.employee_details()
    emp3.employee_details()
    city="Los Angeles"
    
    
if __name__=="__main__":
    main()
    
        