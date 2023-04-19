'''
1. take input from the user cost price and the selling price and find if its a 
profit/loss/no profit no loss along with amount of profit/loss
 
2. take base and height of right angle triangle and find the hypoteneous
 
3. take input from user first name and last name and concatenate to full name and find the 
total number of chars in full name
 
4. take principle, rate and time from the user and find Simple interest
 
5. find the max and min value amoung 3 values take from the user. do not use min and max
inbuild functions. 
'''
from math import sqrt
actual_cost= float(input('Enter cost price'))
sale_cost= float(input('Enter sale price'))
if (actual_cost>sale_cost):
    amount = actual_cost-sale_cost
    print("{}amount loss incurred".format(amount))
elif (sale_cost>actual_cost):
     amount = sale_cost-actual_cost
     print("{} amount profit incurred".format(amount))
else:
    print("No profit or loss")
    
base= eval(input("ENter  base"))
height= eval(input("Enter height"))
hypotenuse= sqrt(base*base+height*height)

print ("the hypotenuse is",hypotenuse )

    
first_name=input('Enter first name')
last_name=input('Enter last name')
fullname =first_name+last_name
print("Your full name is ",fullname)

principal = int(input('ENter the principal'))
rate = int(input('ENter the rate'))
time = int(input('ENter the time'))
simpleinterest = (principal*rate*time)/100
print(" the simple interest is {} ".format(simpleinterest))

a = int(input('ENter one number'))
b = int(input('ENter 2nd number'))
c = int(input('ENter 3rd number'))

if(a>c) and (a>b):
        print ("one number in max ",a)
elif (c>a) and (c>b):
     print ("3rd number in max ",c)
else:
     print ("2nd number in max ",b)
        
