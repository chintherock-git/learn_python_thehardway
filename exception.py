try:
    #import ggg
    #print(a)
    #x=4/0
    #fo=open("ggg.txt")
    v="8"+"ggg"
    age=30
    assert age>32
#Assertion is used for self defined conditions
except  AssertionError:
    print("The age is less than 32")
except TypeError:
    print("You have picked wrong types")
except ZeroDivisionError:
    print("Its a division by Zero")
except ModuleNotFoundError:
    print("The module is not found")
except Exception as e:
    print("There is some issue in Run time",e)
else:
    print("Congrats!!! you got output without any runtime exception")
finally:
    print("This will execute")
