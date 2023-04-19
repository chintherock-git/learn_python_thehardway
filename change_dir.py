import os

print("Current working directory {}".format(os.getcwd()))
print("Parent Directory {}".format(os.pardir))
#change to parent directory
os.chdir(os.pardir)
print("Current working Directory changed to parent {}".format(os.getcwd()))

l=list(range(0,5))
l1=list()
for i in l:
    if i==1:
     l1.append(l[i])
    elif i==2:
        l1.append(l[i]+l[i])
    else:
        l1.append(l[i-1]+l[i-2])
        
print(l)
print(l1)

#valid credit card
import sys,re
class validate_creditcard():
  def __init__(self):
    self.__creditcard=0
    attempt,flag=0,0
    while attempt<3 and flag:
      self.__creditcard = input("Enter the credit card ")
      try:
        assert self.__creditcard.count()==5, "Value cannot be more than 5"
        mid=len(self.__creditcard)
        sum=int(self.__creditcard[mid-1]+self.__creditcard[mid])
        count_upper,count_lower,count_space,count_special=0,0,0,0
        regex= re.compile('[!@#$%^&*()_+~{|":;><}]')
        for i in self.__creditcard:
          if i.isupper():
            count_upper=count_upper+1
          elif i.islower():
            count_lower=count_lower+1
          elif i.isspace():
            count_space=count_space+1
          elif regex.search(self.__creditcard)==None:
            count_special=1
        assert count_upper()==0,"Value does not contain upper case"
        assert count_lower()==0,"Value should not contain lower case"
        assert count_space()==0, "Value should not be space"
        assert count_special==0, "Value should not be special"
        assert self.__creditcard[0]==0, "Value should not start with 0"
        assert self.__creditcard[-1]==0, "Value should not end with 0"
        assert sum%2!=0,"Middle sum should be odd"

      except:
        print(sys.exc_info()[1])
      else:
        print("credit card is valid")
        flag=1
    attempt+=1
if flag ==0:
    print("All Attempts exhausted")

obj=validate_creditcard()