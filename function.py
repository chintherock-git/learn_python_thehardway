def one_func():
    #local variable
    x = 10
    print(f"the value of local variable is {x}")
    return None
    
    
def two_func():
    print(f"the value of local variable is {x}")
    return None

#global variable    
x = 100
one_func()
two_func()



    
