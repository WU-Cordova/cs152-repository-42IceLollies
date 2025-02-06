from projects.project1.card import Card
import random
from datastructures.bag import Bag

# Make deck a numpy array for efficiency

class Multideck:
    # creates a base deck which belongs to the class - to be copied into specific game decks
    suits = ["diamonds", "hearts", "spades", "clubs"]
    faces = [i for i in range(2,10)] + [i for i in['A', 'J', 'Q', 'K']]
    vals = [i for i in range(2,10)] + [i for i in [(1,11), 10,10,10]]
   


    def __init__(self):
        """creates a new bag of 2,4,6, or 8 decks for the game"""
        
        self.__num_decks = random.choice([2,4,6,8])
        self.__multideck = Bag()
        for i in range(self.__num_decks):
            [self.__multideck.add(Card(Multideck.faces[i], Multideck.vals[i], Multideck.suits[i//(len(Multideck.faces)//4)]))  for i in range(len(Multideck.faces))]


    
    def deal(self):
        """Removes a random card from the deck bag and returns it"""
        while len(self.__multideck)>0:
            # picks a card
            card = random.choice(list(self.__multideck.distinct_items()))
            # checks if its in the deck still
            if self.__multideck.__contains__(card):
                # removes from the deck and returns it
                self.__multideck.remove(card)
                return card

    


