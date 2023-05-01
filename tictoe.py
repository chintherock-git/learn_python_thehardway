
class TicToe:
    row0 = ['','','' ]
    row1 = ['','','' ]
    row2 = ['','','' ]
    
    def __init__(self):
        pass
    
    def display(self):
        print(TicToe.row0)
        print(TicToe.row1)
        print(TicToe.row2)
        
    def playgame(self):
        while True:
            choice=input("Do u want to play game ...Enter Y or N ")
            if choice not in ['Y','N']:
                print("Please enter Yor N")
                continue
            break
        if choice=='Y':
            return True
        else:
            False
        
    def takeUserInput(self):
        print("Welcome to Tic Tao")
        player_one_symbol =input("Player 1!! Choose 'X or O'")
        if player_one_symbol=='X':
            player_two_symbol='0'
        else:
            player_two_symbol='X'
        print(f"Good you have chosen {player_one_symbol}")
        while TicToe.playgame(self):
            try:
                acceptable_range=range(0,3)
                row=int(input("Enter the row number "))
                while row not in acceptable_range:
                    print("Row number entered is not within 0-3(not inclusive)")
                    row=int(input("Re Enter the row number "))
                    if row in acceptable_range:
                        break
                    continue
                col= int(input("Enter the column number "))
                while col not in acceptable_range:
                    print("Column number entered is not within 0-3(not inclusive)")
                    col=int(input("Re Enter the col number "))
                    if col in acceptable_range:
                        break
                    continue
            except ValueError:
                print("Error Occured")
                print("Enter String for Symbol and Integer between 0-2 for row and col")
                continue
            else:
                break
            finally:
                print("Player 1 turn")
        list_input=[player_one_symbol,row,col]
        return list_input

    def update_tictoe(self,list_user1):
        symbol=list_user1[0]
        if list_user1[1]==0:
            if list_user1[2]==0:
                TicToe.row0[0]=symbol
            elif list_user1[2]==1:
                TicToe.row0[1]=symbol
            elif list_user1[2]==2:
                TicToe.row0[2]=symbol
        elif list_user1[1]==1:
            if list_user1[2]==0:
                TicToe.row1[0]=symbol
            elif list_user1[2]==1:
                TicToe.row1[1]=symbol
            elif list_user1[2]==2:
                TicToe.row1[2]=symbol
        elif list_user1[1]==2:
            if list_user1[2]==0:
                TicToe.row2[0]=symbol
            elif list_user1[2]==1:
                TicToe.row2[1]=symbol
            elif list_user1[2]==2:
                TicToe.row2[2]=symbol
            
            
            
if __name__=="__main__":
    c=TicToe()
    c.display()
    l=c.takeUserInput()
    c.update_tictoe(l)
    c.display()
            