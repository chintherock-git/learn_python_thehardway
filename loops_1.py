import datetime_1
import os

path_input = input("Enter path to find the list of files or directories ")
ext = input("Enter the file extension you want to search in path provided ")
no_file=0

if (os.path.exists(path_input)):
    print("User has entered a valid path")
    if (os.path.isdir(path_input)):
         print("User has entered a valid path of directory")
         dirname=os.path.dirname(path_input)
         print(dirname)
         list_dir_contents = os.listdir(path_input)
         print("The contents of dir are")
         for each in list_dir_contents:
             #print(each+"\n")
             #file_path = dirname+os.sep+each
             file_path=os.path.join(dirname,each)
             print(f"The file {file_path} was created before {datetime_1.return_actualdaysoffilecreation(file_path)} "+" days")
             if each.find(".")!=-1:
                 if each.endswith(ext):
                     print("Match",each)
                     no_file=no_file+1
                 else:
                      print("No Match",each)
             else:
                 print("Directory and not file",each)
    elif (os.path.isfile(path_input)):
        print("User has entered a valid path of file")
        file_name = os.path.basename(path_input)
        if file_name.endswith(ext):
            print ("The user entered path is the name of the file the user searched for")
            print(f"The file name is {file_name}")
else:
     print("User has not entered a valid path....ReTry!!!")
     
print(f"The total number of files that matches the extension {ext} is {no_file}")