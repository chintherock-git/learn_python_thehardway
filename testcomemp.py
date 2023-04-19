from Company import Company
from Employee import Employee
import unitest,Employee,re
e =Employee()
e.setName()
e.setSalary()
e.show_data=-0  ,
class TestEmployeeCompany(unittest.TestCase):

  def setUp(self):
    self.e=Employee()
    self.c=Company()
  
  def testCompanyName(self):
    '''Company Name'''
    c_name=self.c.com_name.lower()
    self.asserTrue(c_name=="ibm" or c_name=="microsoft" or c_name="accenture")

  def testCompanyLocation(self):
    locations=['delhi','mumbai','bangalore']
    companylocation=c.com_loc.lower()
    self.assertTrue(companylocation in locations)

  def testvowel(self):
      regex='^[aeiou]*'
      if (re.search(regex,e.emp_name.lower())):
            result = True
      else:
            result = False
      self.assertTrue(result==True)

  def testSalary(self):
    self.assertTrue(e.emp_sal>20000)

  def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestEmployeeCompany("testvowel"))
    my_suite.addTest(TestEmployeeCompany("testSalary"))
    my_suite.addTest(TestEmployeeCompany("testCompanyLocation"))
    my_suite.addTest(TestEmployeeCompany("testCompanyName"))
    return my_suite


  if __name__=='__main__':
    runner =unitestesr.TextTestRunner()
    test_suite=suite()
    runner.run(test_suite)
