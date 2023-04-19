import sys

arg_len=len(sys.argv)

if arg_len!=3:
    print(f"You have not entered correct no. of arguments")
    print(f"Enter for {sys.argv[0]} <your req string> and the <req format>")    
    sys.exit()

user_string=sys.argv[1]
user_format=sys.argv[2]

if user_format=="lower":
    print(user_string.lower())
elif user_format=="upper":
    print(user_string.upper())
elif user_format=="title":
    print(user_format.title())
else:
    print("Please enter a valid option\n")
