def func_1():
    return None

def _add_numbers(a,b):
    return a+b

def func_2():
    number1 = eval(input("enter first number"))
    number2 = eval(input("enter 2nd number "))
    func_1()
    print("the sum is {}".format(_add_numbers(number1,number2)))
    print("the product is ",_multiply_numbers(number1))
    return None

'''function with default args
Rule 1 Non default arguments follow default arguments
a and b are positional arguments'''
def _multiply_numbers(a,b=1):
    return a*b
    
func_2()
#__name__ built on variable by default has value __main__inside the same script
print("the value of the variable __name__ is ",__name__)