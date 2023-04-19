class Choices():
    def __init__(self,name,c):
        self.name=name
        self.choice=c
    @property
    def choice(self):
        return self.__choice
    @choice.setter
    def choice(self, val):
        if val>2 and val<=3:
            self.__choice=3
        elif val>3 and val<=6:
            self.__choice=6
        else:
            self.__choice=1

if __name__=='__main__':
    c=Choices('chinmayee',4)
    print(c.choice)