from projects.project3.drink import Drink
from datastructures.array import Array

class Menu:

    def __init__(self, drinks: list[Drink])-> None:
        self.menu = Array(starting_sequence= drinks, data_type = Drink)


    def print_menu(self)-> None:
        for drink in self.menu:
            print(drink)