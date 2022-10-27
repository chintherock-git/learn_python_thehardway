import argparse
parser=argparse.ArgumentParser(description="calculates the power")
group=parser.add_mutually_exclusive_group()
#optionla arguments acting as flags
#mutually exclusivemeans noth cant be used together
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q","--quiet",action="store_true")
#positional arguments
parser.add_argument("x",type=int, help="this is the base")
parser.add_argument("y",type=int,help="this is the component")
args=parser.parse_args()
answer=args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} is {}".format(args.x,args.y,answer))
else:
    print("{}^{}={}".format(args.x,args.y,answer))
