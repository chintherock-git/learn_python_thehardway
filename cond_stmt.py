#!/usr/local/bin/python3

_even= [0,2,4,6,8,10]
_check_memebership = eval(input("Enter a number to check its membership in even list"))


#Conditional stmt with membership check
if _check_memebership in _even:
    print(f"This even number has its presence in the list")
    
_words = eval(input("Enter number to get the word value"))

my_words  = {1:'one',2:'two',3:'three',4:'four',5:'five'} 

if _words not in range(1,5):
    print(f"User entered value {_words} to fetch word is not in range")
else:
    print (my_words.get(_words))

#all and any as list of logical operators
#example of  conditional if elif else with no paranthesis
if all([1<2,2<3,4<5]):
    print("Expressions in List are all true")
if any([1>2,3>2,4>5]):
    print("Any one of the Expressions in List is true")
else:
    print("Not checking all or any")