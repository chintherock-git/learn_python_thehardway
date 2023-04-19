import unittest,math
rad = int(input("Enter radius of the circle"))
def area(rad):
    return math.pi*rad**2

def perimeter(rad):
    return math.pi*rad*2
class SimpleClass(unittest.TestCase):
    def testarea(self):
        self.assertEqual(area(4)>20,True)
        
    def testperimeter(self):
        self.assertEqual(perimeter(4)>20,True)
if __name__=='__main__':
    unittest.main()
    