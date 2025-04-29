from projects.project3.drink import Drink
from datastructures.array import Array
import copy
import time



class Menu:

    def __init__(self, drinks: list[Drink])-> None:
        self._menu = Array(starting_sequence= drinks, data_type = Drink)


    def print_menu(self)-> None:
        for i in range(len(self._menu)):
            print(f"({i+1})  {self._menu[i]}")
        input("\n Press enter to return to main menu.")

    def order(self, drink_ID: str|int) -> Drink:
        try:
            new_drink = copy.deepcopy(self._menu[drink_ID-1] if type(drink_ID) == int else self._menu[self._menu.index(drink_ID)])
        except IndexError:
            raise ValueError("Drink not found in menu.")
        new_drink.generic = False
        return new_drink
    




bistro_menu = Menu([Drink(True, "Black Hole", 5.00), Drink(True, "London Fog", 5.25), 
                    Drink(True, "Latte", 4.50), Drink(True, "Matcha", 5.50), Drink(True, "Hot Tea", 4.00)])