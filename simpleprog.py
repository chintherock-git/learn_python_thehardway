import os
'''def quad_sol(a=1,b=1):
 return  (a**2+b**2+2*a*b)

sol = quad_sol(3,4)
print(f" the quadratic solution of (a+b)**2 is {sol}") 

def swap(a,b):
    sum = a+b
    b = sum-b
    a = sum-b
    print(f"swapped numbers are a = {a}, b = {b}")
    
    
a = eval(input("Input first number"))
b = eval(input("Input 2nd number"))
swap(a,b)

#random  number s in python
#both numbers are inclusive
import random

rand= random.randint(0,3)
print(f"the random number is {rand}")


a = input ("Enter a character ")

while a!='z':
    print(f"you have entered {a}")
    a = input ("Enter any character or Enter z to exit")
    
a =1

while a <10:
    print(f"{a} is less than 10")
    a= a+1'''


path =  "/usr/local/bin"
l=os.listdir(path)
for each in l:
    final_path=os.path.join(path,each)
    if os.path.isdir(final_path):
        print(f"{each} ts a dir")
    elif os.path.isfile(final_path):
        print(f"{each} its a file")
    else:
        print(f"{each} not dir nor file")
        
r= requests
        

    

    
