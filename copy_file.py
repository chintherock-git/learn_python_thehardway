import os.path
src_file =  input ("Enter the source file to copy the content \"FROM\"")
dest_file =  input ("Enter the dest file to copy the content \"TO\"")


if (os.path.exists(src_file) and os.path.isfile(src_file)):
    print("The user input for src is an existing file")
    if (os.path.exists(dest_file) and os.path.isfile(dest_file)):
        print("The user input for dest is an existing file")
    else:
        print("User input for dest file is not valid")
else:
    print("User input for src file is not valid")
    
fs = open(src_file)
fd = open(dest_file,'w')

data = fs.readlines()
fd.writelines(data)

fs.close()
fd.close()

    
    
    
    

