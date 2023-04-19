def fun_sum(*args):
    list_even=[]
    for each in args:
        if each%2==0:
            list_even.append(each)
    print("the even numbers entered by user as arguments is",list_even)
    return len(args)

def string_format(sample):
    count=0
    sample_list=""
    for each in sample:
        if (count%2==0):
            sample_list=sample_list+each.upper()
        else:
            sample_list=sample_list+each.lower()
        count+=1
    return sample_list
def reverse_word_list(sample):
    sample_wordlist=sample.split()
    reverse_list=sample_wordlist[::-1]
    reverse_list=' '.join(reverse_list)
    return reverse_list

def find33(number_list):
    flag=False
    index=0
    start=0
    while index<len(number_list) and start<len(number_list):
        index=number_list.index(3,start)
        if index<len(number_list):
            if (number_list[index+1]==3):
                flag=True
                break
            else:
                start=index+2
        else:
            break
    return flag

def pattern():
    s = [1,7,9,7,0,9,7]
    flag=False
    pattern1=[0,0,7,'x']
    for i in s:
        if i == pattern1[0]:
            pattern1.pop(0)
    return len(pattern1)==1

def city_scope():
    city="mula"
    print("local scope",city)
    def city_scope1():
        nonlocal city
        city="nonloocal"
        print(city)
    city_scope1()
    
def isprime(n):
    prime_list=[]
    count=0
    if n in [0,1]:
        return ""
    for i in range(2,n):
        if n%i==0:
                count=1
                break
    if count<1:
     return n
    else:
        return ""
    

def main():
   # print("The number of argumenyts passed to fun_sum function is",fun_sum(3,3,4,5,6,8,2,4,5,5,3,4,5))
   # sample="mhinkilyifgrtbgyshnbs"
    #print("Formatted String",string_format(sample))
   # print("Reverse of the sentence",reverse_word_list("Kya hua tera wada"))
   #print("consecutive 3, 3 in List is ",find33([1,2,3,2,7,3,3]))
   print(pattern())
   global city
   city="kula"
   city_scope()
   print(city)
   prime_list=[]
   for i in range(100):
    prime_list.append(isprime(i))
    prime_list_only=[]
   for i in prime_list:
    if i!="":
        prime_list_only.append(i)
   print(len(prime_list_only))

if __name__=='__main__':
    main()