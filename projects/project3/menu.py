from projects.project3.drink import Drink
from datastructures.array import Array
import copy
import time



class Menu:

    def __init__(self, drinks: list[Drink])-> None:
        """Initializes a menu object, holding all provided drinks"""
        self._menu:Array = Array(starting_sequence= drinks, data_type = Drink)


    def print_menu(self)-> None:
        """Prints out a string representation of the menu items with prices"""
        print("\n\n")
        for i in range(len(self._menu)):
            print(f"({i+1})  {self._menu[i]} (M)")
        input("\n Press enter to return to main menu.")



    def order(self, drink_ID: str|int) -> Drink:
        """Takes in the number or name of a drink and returns the corresponding drink object from the menu"""
        try:
            new_drink:Drink = copy.deepcopy(self._menu[drink_ID-1] if type(drink_ID) == int else self._menu[self._menu.index(Drink(True,drink_ID, None, None))])
        except IndexError:
            raise ValueError("Drink not found in menu.")
        new_drink.generic = False
        return new_drink
    



# Current Hardcoded Menu for the Bistro

bistro_menu = Menu([Drink(True, "Black Hole", 5.00), Drink(True, "London Fog", 5.25), 
                    Drink(True, "Latte", 4.50), Drink(True, "Matcha", 5.50), Drink(True, "Hot Tea", 4.00)])