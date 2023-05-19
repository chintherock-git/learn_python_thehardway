import random

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
           'Jack':11,'Queen':12,'King':13,'Ace':14}
suit_list=('Heart','Diamond','Club','Spade')
rank_list=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit
    
    def __str__(self):
        return self.rank+" of "+self.suit
    
    
if __name__=='__main__':
    two_heart=Card('Heart','Two')
    print(two_heart)
    print(two_heart.get_rank())
    print(two_heart.get_suit())
    print(two_heart.value)
    king_heart=Card('Heart','King')
    print(king_heart.value==two_heart.value)
    
    
    