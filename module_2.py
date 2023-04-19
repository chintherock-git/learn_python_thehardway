#!/usr/local/bin/python3
import module_1
import getpass

print(module_1.my_space)
password=getpass.getpass(prompt="Enter the password ")
print (f"the password entered is {password}")
print(getpass.getuser())
 

