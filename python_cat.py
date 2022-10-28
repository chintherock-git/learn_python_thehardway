import argparse

parser=argparse.ArgumentParser(description="reimplementation of cat")

parser.add_argument('-n', '--number', action='store_true')
parser.add_argument('file1', type=str,help='first file')
args=parser.parse_args()
print("arguments are", args)
count=0

if args.number:
        with open(args.file1) as f:
         for line in f: 
           count+=1
           print("{} line is {}".format(count,line.strip()))
           
else:
   with open(args.file1,'r') as f:
    for line in f:
     print(line.strip())
     
     
 #command to run python3.11 python_cat.py file1.txt
 #command to run with both positional and optional arguments python3.11 python_cat.py -n file2.txt