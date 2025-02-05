from dataclasses import dataclass

class Card:

    def __init__(self, face, value, suit):
        self.__face = face
        self.__value = value
        self.__suit = suit

    @property
    def face(self):
        return self.__face
    
    @property
    def value(self):
        return self.__value
    
    @property 
    def suit(self):
        return self.__suit

    
    