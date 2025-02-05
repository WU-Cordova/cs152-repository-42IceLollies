from projects.project1.card import Card
from typing import Optional, Iterable

class Player:
    """I made this before realizing there would only be two players, but I'm proud of getting the decorators to work, so I'm keeping it"""

# change list to bag??
    def __init__(self, name:str, *cards: Optional[Iterable[Card]] ):
        self.__name = name
        self.__hand = []
        [self.__hand.append(i) for i in cards]

    @property
    def hand(self):
        return self.__hand

    @property
    def name(self):
        return self.__name
    
    @hand.setter
    def add(self, new_card: Card):
        self.__hand.append(new_card)

    @hand.setter
    def clear(self):
        self.__hand = []