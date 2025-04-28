from projects.project3.drink import Drink
from datastructures.array import Array
import copy

class Menu:

    def __init__(self, drinks: list[Drink])-> None:
        self._menu = Array(starting_sequence= drinks, data_type = Drink)


    def print_menu(self)-> None:
        for i in range(len(self._menu)):
            print(f"({i+1})  {self._menu[i]}")

    def order(self, drink_ID: str|int) -> Drink:
        new_drink = copy.deepcopy(self._menu[drink_ID] if type(drink_ID) == int else self._menu[self._menu.index(drink_ID)])
        new_drink.generic = False
        return new_drink