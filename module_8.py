import module_7


#__name__ a variable contain __main__

def abc():
    print("its abc function")

#function defination or defining a function
def main():
    print("My name is chinmayee")
    print(f"NAME variable in module_8 is {__name__}")
    print(f"{module_7.my_name}")
    abc()
    

    
if __name__=='__main__':
    main()  #function calling
    



