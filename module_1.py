#!/usr/local/bin/python3
import os
path ="/Users/apple/RIAQA/CucumberBDD/CucumberJava"
#print(list(os.walk(path)))

for path,dir,file in  os.walk(path,topdown=False):
    print(path,dir)
    print('*'*100)
    for each_file in file:
        if len(each_file)!=0:
            print(each_file)

my_space = 778754542236880908987
my_name = 'chinmayee'
my_location= 'honululu'
