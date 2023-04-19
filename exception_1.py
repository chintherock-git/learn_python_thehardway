

def divide(a,b):
    try:
        c= a/b
    except ZeroDivisionError:
        print("error handled from within a function")
        raise
    
    
def main():
    try:
        divide(8,0)
        a=c+b
        e = 5.0/0.0
        x=input("print a  number")
        z=x+90
        y=int(x)
        assert y<300
        
    except (ZeroDivisionError,NameError):
        print("Change the divisor to something else than 0.0")
        print("Name is not defined")
    except NameError:
        print("Name is not defined")
    except AssertionError:
        print("the number should be less than 300")
    except Exception as e:
        print("Exception has occured")
    else:
        print("Module executed successfully")
    finally:
        print("Module executed fine")
    
if __name__=="__main__":
    main()
    


    
    