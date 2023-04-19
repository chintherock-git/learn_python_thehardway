print("Enter filename to get its content")
filename=input('>')
file_obj=open(filename,'r')

list_content=file_obj.read().split(' ')
print(list_content)

list_length=len(list_content)

for i in list_content:
    print(i) 
    
#print("what\n",list_content)
print("###########################Using While loop##################################")
flag = True
counter=0 
while flag:
    print(list_content.pop(0))
    counter+=1
    if counter==list_length:
        flag=False
    else:
        continue
    

    
    
    
    
    