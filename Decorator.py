

def new_decorator(some_func):
    def wrap_func():
        print("Append some new code")
        some_func()
        print("Do some other stuff")
    return wrap_func

@new_decorator
def some_func():
    print("whatbwill some function do")

some_func()
#greet=new_decorator(some_func)
#greet()

