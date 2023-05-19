import random
import Card_Wargame 
from Card_Wargame import *

class Deck():
    def __init__(self):
        self.deck_allcards=[]
        #for each suit there are 13 ranks
        for suit  in Card_Wargame.suit_list:
            for rank in Card_Wargame.rank_list:
                card_obj=Card(suit,rank)
                self.deck_allcards.append(card_obj)
                
    def shuffle(self):
        random.shuffle(self.deck_allcards)
    
    def getcard_deck(self):
        return self.deck_allcards.pop()
                
if __name__=='__main__':
    new_deck=Deck()
    for card in new_deck.deck_allcards:
        print(card)
    new_deck.shuffle()
    print(new_deck.getcard_deck())
    print(len(new_deck.deck_allcards))
    
        