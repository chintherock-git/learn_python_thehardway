

a=6 
b=6

if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a is equal to b")
    
s= 'python'
count =0 
for x in s:
    print(f"Index {count}---{x}")
    count+=1
    
_list =  'KRISHNA'

print (" the length of the string",len(_list))
for each in list(range(len(_list))):
    print(f"Index value of _list[{each}]",_list[each])

i=0
    
while i!=10:
    i = i+1
    if i==5:
        continue
    print (f"value of i is  {i}")