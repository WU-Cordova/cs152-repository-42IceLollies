from projects.project3.drink import Drink
from datastructures.array import Array

class CustomerOrder:
    
    def __init__(self, name:str = None, drinks:Array[Drink] = Array(data_type=Drink)) -> None:
        """Initiates a Customer's order, starting with the first provided information (Name or drink)"""
        self._name: str = name
        self._drinks: Array[Drink] = drinks
        self._price: float = 0
        self._fulfilled: bool = False

        for drink in self._drinks:
            self._price += drink.price

    
    def add_drink(self, new_drink: Drink)-> None:
        """Adds a new drink to the running order and adds the price to the total"""
        self._drinks.append(new_drink)
        self._price += new_drink.price

    def finish(self) -> None:
        """Marks that the order has been fulfilled"""
        self._fulfilled = True

    def __str__(self) -> str:
        """Returns a string representation of the Customer's order"""
        return f"Here's what we have for your order: \n Name: {self._name if self._name else "?"} \n Order: {", ".join([str(self._drinks[i]) for i in range(len(self._drinks))])}\n Total: {self._price}"
    

    