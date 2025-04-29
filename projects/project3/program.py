# DOCSTRINGS
# DRINKS SHOULD HAVE SIZES BUT ONLY SIZE MEDIUM
# TYPEHINTS ON DECLARED VARS
# FOR SOME REASON IT ALLOWS NEGATIVE MENU ITEMS???
# TIMEOUT FOR STUFF???
# WAY TO EXIT FROM LOOPS IF ACCIDENTALLY ENTERED N TO EDIT ORDER

from projects.project3.menu import Menu, bistro_menu
from projects.project3.drink import Drink
from projects.project3.customer_order import CustomerOrder
from projects.project3.bistro_system import Bistro_System
import time

def main():
    
    bistro_sys = Bistro_System()
    
    # list of actions, will be referenced by index number
    actions = [bistro_menu.print_menu, bistro_sys.take_order, bistro_sys.print_open_orders, bistro_sys.complete_order, bistro_sys.print_day_stats, quit]

    # main while loop - loops until user exits program
    while(True):

        # prints the menu, receives a response from the user, and executes the action associated with that response
        try:
            actions[bistro_sys.print_main_menu()-1]()
            print("\n\n\n")
        # if there is a typo, asks again
        except ValueError:
            print("\nERROR. Please enter your number numerically (e.g. 1, 2, 3, etc.)")
            time.sleep(2)



        



    # TESTING STUFF (DELETE)
    # new_menu = Menu([Drink(True, "Black Hole", 5.00), Drink(True, "London Fog", 5.25), 
    #                 Drink(True, "Latte", 4.50), Drink(True, "Matcha", 5.50), Drink(True, "Hot Tea", 4.00)])
    # # new_menu.print_menu()

    # test_order = CustomerOrder(name= "Sophieophie", drinks = [new_menu.order("Latte")])
    # print(test_order)



if __name__ == '__main__':
    main()
