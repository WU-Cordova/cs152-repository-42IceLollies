from dataclasses import dataclass

class Card:

    def __init__(self, face: str|int, value: int|tuple[int], suit: str) -> None:
        """Instantiates a playing card, face down as default"""
        self.__face = face
        self.__value = value
        self.__suit = suit
        # if the card is turned face up, value set to True
        self.__turned = False

    @property
    def face(self) -> str|int:
        """getter for card face property"""
        return self.__face
    
    @property
    def value(self) -> int|tuple[int]:
        """getter for card value property"""
        return self.__value
    
    @property 
    def suit(self) -> str:
        """getter for card suit property"""
        return self.__suit
    
    @property
    def flipped(self) -> bool:
        """returns if the card is face up (True) or face down (False)"""
        return self.__turned
    
    def flip(self) -> None:
        """Switches if the card is face up or face down"""
        self.__turned = not self.__turned
    
    def __str__(self) -> str:
        """Creates a string printout for the card"""
        # if the card is face down, returns a depiction of the back of the card
        if not self.__turned:
            return ("\n _____\n|     |\n|     |\n|     |\n|_____|\n\n")

        # otherwise, returns a depiction of the card based on the suit and face
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

    
    