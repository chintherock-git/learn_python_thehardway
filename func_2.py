import func_1

'''Callingthe keywordbased arguments in function'''
#defination has to be like this
def fun(a,b):
    print("value of a ",a)
    print("valueof b is ",b)
    
def func_0():
    fun(a=1,b=2)
    #fun(10)
    fun(b=90,a=12)
    
'''function that takes variable length argument and type is tuple'''
    
def func_2(*args):
    print("valueof inputs ",args)
    print("Typeof variable length argument",type(args))
    print("*"*50)
    
'''function with variable length arguments and type is dictionary '''

def func_3(**kargs):
    print("the variable length arguments are",kargs)
    print("the type of variable length argumnet", type(kargs))
    print("*"*50)
    
def main():
    func_0()
    func_2(1)
    func_2(1,2)
    func_2(1,2.0,"hi", True)
    func_3(a=1)
    func_3(a=1,b=3)
    func_3(a=1, b=3.0,c=True,d="chini")
    print("the contents of imported module func_1",dir(func_1))
    print("the value of the variable __name__ for func_2 (current module) is ",__name__)
    print("the value of the variable __name__ for imported module",func_1.__name__)


if __name__=='__main__':
    main()
    



    

