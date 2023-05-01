def inputLoop():
    while True:
        try:
            enter = int(input("Enter a number "))
        except ValueError:
                print("Please enter a integer")
                print("**********************")
                continue
        else:
            break
        finally:
            print("i am gonna execute olwayz")
            
if __name__=="__main__":
    inputLoop()