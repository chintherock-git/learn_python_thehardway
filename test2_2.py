'''_g = "chinmayee"
for i in _g:
    print(i)'''
    
def main():
    list_integers=list()
    while True:
        i = int(input("Enter a number to add to list"))
        if i==0:
            break
        else:
            list_integers.append(i)
    print(f"The list of integers that user has input is {list_integers}")
    #swap first and last element
    i=list_integers[0]
    list_integers[0]=list_integers[-1]
    list_integers[-1]=i
    print(f"List after first and last element swap is {list_integers}")
            
if __name__=='__main__':
    main()
