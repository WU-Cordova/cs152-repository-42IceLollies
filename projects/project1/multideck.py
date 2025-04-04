from projects.project1.card import Card
import random
from datastructures.bag import Bag


class Multideck:
    # creates base deck values which belong to the class - to be copied into specific game decks
    suits = ["diamonds", "hearts", "spades", "clubs"]
    faces = [i for i in range(2,10)] + [i for i in['A', 'J', 'Q', 'K']]
    vals = [i for i in range(2,10)] + [i for i in [(1,11), 10,10,10]]
   


    def __init__(self) -> None:
        """creates a new bag of 2,4,6, or 8 card decks for the game"""
        self.__num_decks = random.choice([2,4,6,8])
        self.__multideck = Bag()
        for i in range(self.__num_decks):
            # adds a single deck
            [self.__multideck.add(Card(Multideck.faces[i], Multideck.vals[i], Multideck.suits[i//(len(Multideck.faces)//4)]))  for i in range(len(Multideck.faces))]


    
    def deal(self) -> Card:
        """Removes a random card from the deck bag and returns it"""
        # while there are cards in the deck
        while len(self.__multideck)>0:
            # picks a card
            card = random.choice(list(self.__multideck.distinct_items()))
            # checks if there are any of this card in the deck
            if self.__multideck.__contains__(card):
                # if it is, removes from the deck and returns it
                self.__multideck.remove(card)
                return card

    


