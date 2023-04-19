s=input('please enter the required string')
def palindrome(s):
    flag=True
    for i in range(0,int(len(s)/2)):
        if(s[i]!=s[-1-i]):
            flag=False
            break
    return flag
lis_pallindrome=[]
print(int(len(s)/2))
for i in range(0,int(len(s)/2)):
    start=0
    end=3+i
    while end<=len(s):
        st=s[start:end]
        if (palindrome(st)):
         lis_pallindrome.append(st)
        start+=1
        end+=1
print(tuple(lis_pallindrome))
            

    