import module_5,os

t=(9,0)
t.count
def main():
    print(f"My name is {module_5.my_name}")
    print(f"My fav book  is {module_5.my_fav_book}")
    print(f"My fav color is {module_5.my_fav_color}")
    cmd="help(sys)"
#print(f"{help(os.system(cmd))}")


if __name__=='__main__':
    main()
else:
    print("calling from import")