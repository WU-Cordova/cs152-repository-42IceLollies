from card import Card
from typing import Optional, Iterable

class Player:

# change list to bag??
    def __init__(self, name, *items: Optional[Iterable[Card]] ):
        self.name = name
        self.hand = []
        [self.hand.append(i) for i in items]

    @property
    def hand(self):
        return self.hand
    
    @hand.setter
    def add(self, new_card: Card):
        self.hand.append(new_card)

    @hand.setter
    def clear(self):
        self.hand = []