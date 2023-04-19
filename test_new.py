
#first modular program in python
'''author:chinmayee
   purpose:this takes input from user'''
   
def main():
    name = input (">>>Enter the line to capitalize : ")
    print(f"The user entered value is {name}")
    title=""
    list_words= name.split(" ")
    print(f" the list of words are {list_words}")
    for word in list_words:
        print(word.capitalize())
        title=title+" "+word.capitalize()
    print(f"The titled sentence is {title}")

if __name__=='__main__':
    main()