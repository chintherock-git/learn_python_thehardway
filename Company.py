class Company:
  
  def __init__(self):
    self.com_name=""
    self.com_location=""
  
  def setName(self):
    name=input(print("Enter Company name"))
    self.emp_name=name

  def setLocation(self):
    sal=(input(print("Enter Company Location")))
    self.emp_sal=sal

  def show_data(self):
    print("Company Name ",self.com_name)
    print("Company Location ",self.self.com_loc)
