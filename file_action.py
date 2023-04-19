
from sys import argv
from os.path import exists

script, filename, target = argv
print ("The script name is {}".format(script))
print("Does the file exist ? {}".format(exists(filename)))
print("The Contents of the file is")
input_data = open(filename, 'r')
print(input_data.read())
print("Reading the firstLine")

#cursor is now at the eof so we have move cursor to beginning to read the fist line
input_data.seek(0)
print(input_data.readline())

print ('*'*10)
print("writing to file")
line1= input("Input text to write to to_file.txt")
#if i wont use a+ then it will overwrite the file
write_data=open(filename,'a+')
write_data.write(line1)
print(write_data.read())


print("Does the target exists {}".format(exists(target)))
target_data= open(target,'w')
inputwrite_data=open(filename,'r')
print("i will be writing {}".format(inputwrite_data.read()))
#cursor again after reading is at the eof and so we have to move the cursor to beginning
inputwrite_data.seek(0)
target_data.write(inputwrite_data.read())
inputwrite_data.close()
target_data.close()

