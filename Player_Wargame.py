from Card_Wargame import Card
from Deck_Wargame import Deck

class Player(): 
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def add_cards(self,card):
        if type(card)==type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} card/s"
    
if __name__=='__main__':
    round_game=0
    game_on=True
    player1=Player("Player1")
    player2=Player("Player2")
    pack=Deck()
    pack.shuffle()
    while len(pack.deck_allcards)!=0:
        player1.add_cards(pack.getcard_deck())
        player2.add_cards(pack.getcard_deck())
    print(player1)
    print(player2)
    while game_on:
        round_game=round_game+1
        print(f"Round {round_game} is on")
        if len(player1.all_cards)==0:
            print ("Player1 looses and is out of cards.Player2 wins")
            game_on=False
            break
        if len(player2.all_cards)==0:
            print ("Player2 looses and is out of cards.Player1 wins")
            game_on=False
            break
        
        #this is the list of cards placed by the player on the table
        player1_cards=[]
        player1_cards.append(player1.remove_one())
        player2_cards=[]
        player2_cards.append(player2.remove_one())
        war_on=True
        while war_on:
            if player1_cards[-1].value>player2_cards[-1].value:
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                war_on=False
            elif player2_cards[-1].value>player2_cards[-1].value:
                player2.all_cards.add_cards(player1_cards)
                player2.all_cards.add_cards(player2_cards)
                war_on=False
            else:
                print("WAR!!!")
        
                if len(player1.all_cards)<3:
                    print("Player 2 Wins")
                    game_on=False
                    break
                elif len(player2.all_cards)<3:
                    print("Player 1 Wins")
                    game_on=False
                    break
                else:
                    for i in range(3):
                      player1_cards.append(player1.remove_one()) 
                      player2_cards.append(player2.remove_one())
                
            
                
                