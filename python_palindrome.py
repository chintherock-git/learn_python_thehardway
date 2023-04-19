s=input('please enter the string')
flag=True
for i in range(0,int(len(s)/2)):
    if (s[i]!=s[-1-i]):
        flag=False
        break
if flag:
  print("palindrome")
else:
  print("no palindrome")
                