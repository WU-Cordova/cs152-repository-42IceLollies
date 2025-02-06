from dataclasses import dataclass

class Card:

    def __init__(self, face, value, suit):
        self.__face = face
        self.__value = value
        self.__suit = suit
        # if the card is turned face up, value set to True
        self.__turned = False

    @property
    def face(self):
        return self.__face
    
    @property
    def value(self):
        return self.__value
    
    @property 
    def suit(self):
        return self.__suit
    
    @property
    def flipped(self):
        return self.__turned
    
    def flip(self):
        self.__turned = not self.__turned
    
    def __str__(self):
        """Creates a string printout for the card"""
        if not self.__turned:
            return ("\n _____\n|     |\n|     |\n|     |\n|_____|\n\n")

        match self.__suit:
            # CREDIT TO SOPHIE AVERY FOR THE IDEA TO DO THIS
            case "diamonds":
                return (f"\n{self.__face} /\\ \n /  \\\n \\  /\n  \\/ {self.__face}\n")
                
            case "hearts":
                return (f"\n{self.__face} /\/\\\n  \\  /\n   \\/ {self.__face}\n")
               
            case "clubs":
                return (f"   _\n{self.__face} /  \\\n  >  <\n \\ /\\ /\n    |  {self.__face}\n")
               
            case "spades":
                return (f"   _\n{self.__face} / \\\n /   \\\n -^|^- {self.__face}\n")

    
    