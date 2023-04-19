import Circle,unittest
class Testing(unittest.TestCase):
    def setUp(self):
        self.o5 = Circle()
 
    def testArea(self):
        self.assertTrue(self.o5.area()>20)
 
    def testCircum(self):
        self.assertTrue(self.o5.circum()>15)
 
if __name__=="__main__":
    unittest.main()
