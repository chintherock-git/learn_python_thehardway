''' The program will create a new file and then add contents to file
by default the open opens the file in read mode, if fiule is not existing then throws error as it will 
not create a new File but write mode will create a new file if not present else it will overwrite'''

#fo = open("src.txt")
fo = open("src.txt",'a')

print (f"Is the file readable ",fo.readable())
print (f"Is the file writable ",fo.writable())
my_content = ["Name is kanha", "Fathers name is Vasudeva", "Mothers name is Devaki", "I love radha", "I am the Absolute Truth"]


for each  in my_content:
    fo.write(each+"\n")
    

    
fo.close()
    
fr= open("src.txt")  
print ("The content of the file is \n",fr.readlines())
fr.close()
