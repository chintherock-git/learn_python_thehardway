'''ques 2:- take input from user any place and print its attraction
if user enters DELHI - we should get Red Fort. Search should be case insensitive
user should get max 3 chance to enter right place. if all attempts fails print "failure"
at any point user enters the right place print its attraction and do not ask again
 
'''

places = ['Delhi', 'Mumbai', 'Chennai', 'Jaipur']
attractions=['Red Fort', 'Gateway of India', 'Marina Beach', 'Amer Fort']

for i in range(len(places)):
    print(places[i]," has an attraction" ,attractions[i])
    
count,found = 1,0
 
while count<=3 and found==0:
    place = input('enter place to get its attraction')
for x in range(len(places)):
    if (place.upper()==places[x].upper()):
        found=1
        index = x
if found==1:
    print("attraction is ",attractions[x])
else:
    print("Not found")
count+=1
        