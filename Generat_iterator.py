import random
import math
def sq_n(n):
    for x in range(n):
        yield x**2
print("**********")      
for i in sq_n(5):
    print(i)
print("**********")
    
b=sq_n(10)
print(next(b))
print(next(b))
print(next(b))

b ="hello"
iter_b=iter(b)
for i in iter_b:
    print(i)
    
def fibonacci():
    a=0
    b=1
    for i in range(10):
        yield a
        a,b=b,a+b

for i  in fibonacci():
    print(i)
    
    
def ran(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
        
for n in ran(2,90,3):
    print(n)
    
    