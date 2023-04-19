from Company import Company
from Employee import Employee
import unittest

class testEmployeeCompany(unittest.TestCase):

  def setUp(self):
    self.e=Employee()
    self.c=Company()
  
  def testCompanyName(self):
    '''Company Name'''
    c_name=self.c.com_name.lower()
    c_name_list=['ibm','microsoft','accenture']
    self.asserTrue(c_name in c_name_list)

  def testCompanyLocation(self):
    locations=['delhi','mumbai','bangalore']
    companylocation=c.com_loc.lower()
    self.assertTrue(companylocation in locations)

  def testvowel(self):
    emp_name=self.e.emp_name
    self.assertTrue(any(char in'aeiou'for char in emp_name.lower()))

  def testSalary(self):
      self.assertTrue(self.e.emp_sal>20000)

  def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(testEmployeeCompany("testvowel"))
    my_suite.addTest(testEmployeeCompany("testSalary"))
    my_suite.addTest(testEmployeeCompany("testCompanyLocation"))
    my_suite.addTest(testEmployeeCompany("testCompanyName"))
    return my_suite


  if __name__=='__main__':
    runner =unittest.TextTestRunner()
    test_suite=suite()
    runner.run(test_suite)
