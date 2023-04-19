import morse

"""  Merging and calculating the sum of two dictionaries: 
    Two dicionaries d1 and d2 with numerical values and
    possibly disjoint keys are merged and the values are added if
    the exist in both values, otherwise the missing value is taken to
    be 0"""

def dict_merge_sum(d1,d2):
    m={}
    len_1=len(d1.keys())
    len_2=len(d2.keys())
    if len_1>len_2:
        m1,m2=d1,d2
    else:
        m1,m2=d2,d1
    for k,v in m1.items():
        if k in m2.keys():
            m[k]=m1[k]+m2[k]
        else:
            m[k]=m1[k]
    for k in m2.keys():
        if k not in m.keys():
            m[k]=m2[k]
    return m


if __name__=="__main__":
    # len(morse.morse)
    # print("a" in morse.morse)
    # print("A" in morse.morse)
    # print(morse.morse["A"])
    # word=input("Enter a phrase ")
    # word_u=word.upper()
    # word_morse=""
    # for each in word_u:
    #     if each not in morse.morse and each !=" ":
    #         word_morse=word_morse+"@"
    #     else:
    #         if each==" ":
    #             word_morse=word_morse+" "
    #         else:
    #             word_morse=word_morse+morse.morse[each] 
    # print(word_morse)
    d2={'one':1,'two':2,'three':3}
    d1={'four':4,'two':90,'three':8}
    print(dict_merge_sum(d1,d2))
    
    
    
        