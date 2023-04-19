##has relation ship no use of inheritence and super keyword
##better and recommended usage


class Other:
    def override(self):
        print("Class OTHER overide")
    def implicit(self):
        print("Class OTHER implicit")
    def altered(self):
        print("Class OTHER altered")

class Child:
    def __init__(self):
        self.other=Other()
    def override(self):
        self.other.override()
        print("Class CHILD overide")
    def implicit(self):
        print("Class CHILD implicit")
    def altered(self):
        pass
    
son=Child()
son.override()
son.implicit()
son.altered()
        