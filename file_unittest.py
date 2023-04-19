import unittest

def add(a,b):
    return a+b
class SimpleClass(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(4,5),)
if __name__=='__main__':
    unittest.main()
    