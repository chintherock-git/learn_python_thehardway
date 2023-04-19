import re
from sys import argv

filename= input("enter the file u want to filter all  numbers")
input_data=open(filename,'r')
numbers = re.findall('[0-9]+', input_data.read())

print("All the numbers in file are {}".format(numbers)) 
