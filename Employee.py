class Employee():
  def __init__(self):
    self.emp_name=""
    self.emp_sal=0
  
  def setName(self):
    name=input(print("Enter employee name"))
    self.emp_name=name

  def setSalary(self):
    sal=float(input(print("Enter employees salary")))
    self.emp_sal=sal

  def show_data(self):
    print("Employee Name ",self.emp_name)
    print("Employee Salary ",self.self.emp_sal)
