from dataclasses import dataclass

@dataclass
class Card:
    face: str
    value: int
    suit: str
    