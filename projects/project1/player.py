from projects.project1.card import Card
from typing import Optional, Iterable

class Player:
    """I made this before realizing there would only be two players, but I'm proud of getting the decorators to work, so I'm keeping it"""
    """It is useful for keeping track of a player's hand"""

    def __init__(self, name:str, *cards: Optional[Iterable[Card]] ) -> None:
        """creates a player instance wiht an empty hand, then adds any cards that have been initially assigned to the player (optional)"""
        self.__name = name
        self.__hand = []
        [self.__hand.append(i) for i in cards]

    @property
    def hand(self) -> list[Card]:
        """getter for the player's hand value"""
        return self.__hand

    @property
    def name(self) -> str:
        """getter for the player's name value"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """setter for the player's name value"""
        self.__name = new_name

    
    def add(self, new_card: Card, flip:bool)-> None:
        """Adds a new card to the player's hand - flips the card according to specification"""
        if flip:
            new_card.flip()
        self.__hand.append(new_card)


    def clear(self) -> None:
        """removes all cards from the player's hand"""
        self.__hand = []