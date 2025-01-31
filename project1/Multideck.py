from Card.py import Card
# is this right???
import random
from bag.py import Bag

# Need to make the number of decks in the multideck different everytime through gameplay 

class Multideck:


    def __init__(self):
        """creates a new set of decks for the game to be played"""
        self.num_decks = random.choice([2,4,6,8])
        suits = [diamond, ]
        self.cards = bag([Card(suit = )])
