def main():
    f1(a=1,b="vini",c=8.0)
    
def string_pangram(s):
    dict_string={}
    flag = True
    string_formatted= s.strip().replace(" ","")
    for each in string_formatted:
        dict_string[each]=string_formatted.count(each)
    print(dict_string)
    for value in dict_string.values():
        if value>1:
            flag=False
            break
        else:
            continue
    return flag

def f1(**kargs):
    print("Hello")
    for each in kargs:
        print(each)
    return None

    
if __name__=="__main__":
    main()
    if string_pangram("The quick brown fox jumps over the lazy dog"):
        print("String is pangram")
    else:
        print("Is not a pangram")
    
