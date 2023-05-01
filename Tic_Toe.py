class TicToeToe():
    
    def __init__(self,playboard=[]):
        self.playboard=playboard
        for i in range(9):
            self.playboard.insert(i,"_")
    
    def display_playboard(self):
        for i in range(9): 
            if i%3==0 and i!=0:
                print("\n")  
            print(f"| " +self.playboard[i]+ " |",end=" ")  
             

    def input_playboard(self,symbol,position):
            self.playboard[position]=symbol
        
    def check_prefilled(self,position):
        filled=True
        if self.playboard[position]!="_":
            filled= False
        return filled
    
    def sublist_position(self,sample):
        sample_len=len(sample)
        sublist=[]
        start=0
        end=3
        while end<=sample_len:
            sub=sample[start:end]
            sublist.append(sub)
            start=start+1
            end=start+3
        return sublist
        
    def check_winner(self):
        win=False
        X_filled=[]
        O_filled=[]
        winning_list=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in range(9):
            if self.playboard[i]=='X':
                X_filled.append(i)
            elif self.playboard[i]=='O':
                O_filled.append(i)
        sublist_x_filled= TicToeToe.sublist_position(self,X_filled)
        sublist_o_filled= TicToeToe.sublist_position(self,O_filled)
        for i in winning_list:
            for sub_list in sublist_x_filled:
                if sorted(sub_list)==i:
                    win=True
                    break
            for sub_list in sublist_o_filled:
                 if sorted(sub_list)==i:
                    win=True
                    break
        return win
    
    def check_Position(self,position):
        check=True
        l=list(range(9))
        if position not in l:
            check=False
        return check
    
if __name__=="__main__":
    
    player="Player 1"
    iteration=1
    game_on=TicToeToe()
    print("Lets play TicToe")
    game_on.display_playboard()
    print()
    try:
        while True:
            print("****" *10)
            symbol=input(f"{player} Enter X or O : ")
            print(symbol)
            #if 'X' not in symbol or 'O' not in symbol:
                #symbol=input("RE-Enter X or O")
            position=int(input("Enter the position in [0-9](9 exclusive)"))
            if not game_on.check_Position(position):
                position=int(input("Enter the position in [0-9](9 exclusive)"))
            if game_on.check_prefilled(position):
                game_on.input_playboard(symbol,position)
                iteration+=1
                game_on.display_playboard()
                if iteration%2==0:
                    player="Player 2"
                else:
                    player="Player 1"
                if iteration>3:
                    if game_on.check_winner(): 
                        print("Congratulations you win!!!")
                        break
                    else:
                        continue
            else:
                position=int(input("Re-nter the position in [0-9](9 exclusive) which is not taken"))
                game_on.input_playboard(symbol,position)
                iteration+=1
                game_on.display_playboard()
                if iteration%2==0:
                    player="Player 2"
                else:
                    player="Player 1"
                if iteration>3:
                    if game_on.check_winner():
                        print("Congratulations you win!!!")
                        break
                    else:
                        continue     
    except ValueError:
        print("Enter Integer for Position")
            
            

