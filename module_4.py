#!/usr/local/bin/python3
try:
    import os, os.path,sys
    input_len = len(sys.argv)
    if input_len!=2:
        print(f"Please enter one input i.e your path")
    else:
        path=sys.argv[1]    
        print("*"*100)
        #deliberately putting a false assertion
        assert path.find("/")==-1  
        print(f"User entered path: {path}")
        print(f"Is it a File ? \n Answer: {os.path.isfile(path)}")
        print(f"Is it a Directory ? \n Answer: {os.path.isdir(path)}")
        print(f"What is the basename ? \n Answer: {os.path.basename(path)}")
        print(f"What is the directory ? \n Answer: {os.path.dirname(path)}")
        print(f"Does the file/dir exist ? \n Answer: {os.path.exists(path)}")
        print(f"Splitting the path ?\n Answer: {os.path.split(path)}")
        path_split= os.path.split(path)
        print(f"Joining the tuple components... \n Answer :{os.path.join(path_split[0],path_split[1])}")
        print("*"*100)
        print(os.system("date"))
except FileNotFoundError as e:
    print("Users input is not valid",e)
except AssertionError as e:
    print("Ur assertion user defined check failed")
else:
    print("There are no runtime exception")
finally:
    print("Congrats you successfully checked the status!!!")