'''
take input from user any string and print its middle char
if number of chars in a string are even, print 2 middle elements
else one middle element
 
'''

fullname = input('please enter your full name')

length=len(fullname)
middle = int(length/2)
if (int(length%2==0)):
    print(fullname[middle-1]+fullname[middle])
else:
    print(fullname[middle])
    