'''
ques 1
take_input function - take input from user radius of a circle, length 
and breadth of rectangle
calculate_area - find area of circle and rectangle and print
calculate_perimeter - find perimeter of circle and rectangle and return to 
main and print
 
ques 2
take input from user CP and SP in take_input function.
in calculate function find if its a 
profit/loss/no profit no loss along with amount of profit/loss
DONOT print any answer in this function
 
print final answer in main
'''
from math import pi
def returnarea_perimeter(rad, length,breadth):
    area_circle = pi*rad*rad
    per_circle= 2*pi*rad
    area_rect= length*breadth
    per_rect=2 (length+breadth)
    print (" Area of circle is ",area_circle)
    print (" Perimeter of Circle is ",per_circle)
    print (" Area of Rectangle  is ",area_rect)
    print (" Perimeter of Rectangle is ",per_rect)