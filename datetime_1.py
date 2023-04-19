#install pytz moduleusing command pip3 install pytz towrkwith timezones
import os.path
from datetime import datetime

'''This program gives the details of the no. of days from current date from which the files were created'''
_dir_path = input("Enter path of folder")

def return_actualdaysoffilecreation(a):
    _diff_days = 0
    _currentutc_dateformat = datetime.strptime((datetime.utcnow().strftime("%Y-%m-%d")),"%Y-%m-%d")
    if os.path.exists(a):
        print("Its a valid path")
        if os.path.isdir(a):
         print("Its a path of a dir")
        elif os.path.isfile(a):
            print("Its a path of a file")
            _creation_timetamp = os.path.getctime(a) #givestimestamp
            _creation_utctime = datetime.utcfromtimestamp(_creation_timetamp) #gives UTC
            _creation_strformat = _creation_utctime.strftime("%Y-%m-%d") #returns string
            _creation_dateformat= datetime.strptime(_creation_strformat,"%Y-%m-%d")#returns datetimeobj
            _delta = _currentutc_dateformat-_creation_dateformat
            _diff_days=_delta.days
    else:
        print("Re.try with valid path")
    return _diff_days

#days = return_actualdaysoffilecreation(_dir_path)
#print (f" The file was created {days} from today")