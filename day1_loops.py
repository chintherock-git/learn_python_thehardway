'''
take first name and last name from the user and concatenate to full name with one space
in between
1. find total number of upper case letters in a full name
2. find total number of lower case letters in a full name
3. find total number of digits if any in a full name
4. find total number of special chars if any in a full name
5. find total number of spaces in full name
6. find total number of chars in full name including spaces and special chars
7. find total number of lower case vowels in full name
'''


count_digit=0
count_char=0
count_lower_vowel=0
count_space=0
count_special=0
count_lower=0
count_upper=0
first_name = input('print enter first name')
last_name = input ('please enter last name')
full_name = first_name+" "+ last_name 
for x in full_name:
    count_char+=1
    if x.isdigit():
        count_digit+=1
    elif (x in 'aeiou'):
        count_lower_vowel+=1
    elif x.isspace():
        count_space+=1
    elif x.islower():
        count_lower+=1
    elif x.isupper():
        count_upper+=1
    else:
        count_special+=1
    
print("{} Count of total characters ".format(count_char))    
print("{} Count of Digit ".format(count_digit))
print("{} Count of Lower char ".format(count_lower))
print("{} Count of Upper char ".format(count_upper))
print("{} Count of Special char".format(count_special))
print("{} Count of lower case vowel ".format(count_lower_vowel))
print("{} Count of Space ".format(count_space))