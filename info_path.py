import os, time
from sys import argv

path = input('Enter the path to fetch the details ')
stat_info=os.stat(path)
print(stat_info)
print ("Size: {}".format(stat_info.st_size))
print ("Permission: {}".format(stat_info.st_mode))
print ("Owner: {}".format(stat_info.st_dev))
print ("Device: {}".format(stat_info.st_dev))
#time.ctime converts sec  since epoch into local time
print ("Created Time: {}".format(time.ctime(stat_info.st_ctime)))
print ("Last Modified  Time : {}".format(time.ctime(stat_info.st_mtime)))
print ("Last Accessed Time : {}".format(time.ctime(stat_info.st_atime)))




