def local():
    #name= "local"
    
    def nested_local():
        nonlocal name
        name="nested_local"
    print("Global inside function scope ",name)
    nested_local()
    print("Nested Local scope ",name)

def main():
   name="OM SHREE GANESH"
   local()
   print("Main ",name)

if __name__=='__main__':
    main()
    